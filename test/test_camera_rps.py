import os, sys
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import cv2

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "../..", "computer-vision-rock-paper-scissors30"
        )
    )
)
from main.camera_rps import RockPaperScissorsGame


# Mock Keras model and prediction
mock_model = MagicMock()
mock_model.predict.return_value = np.array(
    [[0.0, 0.0, 0.0, 1.0]]
)  # Simulate prediction for "Scissors"
model_path = "converted_keras/keras_model.h5"
labels_path = "converted_keras/labels.txt"
# Load class labels
with open(labels_path, "r") as file:
    mock_class_names = [line.strip().split(" ")[1] for line in file.readlines()]


class TestRockPaperScissorsGame(unittest.TestCase):
    @patch("cv2.VideoCapture")
    def setUp(self, mock_video_capture):
        self.mock_cap = MagicMock()
        mock_video_capture.return_value = self.mock_cap
        self.mock_cap.isOpened.return_value = True

        # Initialize the game with the mocked model and class names
        self.game = RockPaperScissorsGame(model_path, labels_path)
        self.game.model = mock_model
        self.game.class_names = mock_class_names

    def test_preprocess_image(self):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        preprocessed_image = self.game.preprocess_image(frame)
        self.assertEqual(preprocessed_image.shape, (1, 224, 224, 3))

    def test_get_prediction(self):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        predicted_label = self.game.get_prediction(frame)
        self.assertEqual(predicted_label, "Scissors")

    def test_determine_winner_user_wins(self):
        result = self.game.determine_winner("Rock", "Scissors")
        self.assertEqual(result, "user")

    def test_determine_winner_computer_wins(self):
        result = self.game.determine_winner("Rock", "Paper")
        self.assertEqual(result, "computer")

    def test_determine_winner_tie(self):
        result = self.game.determine_winner("Rock", "Rock")
        self.assertEqual(result, "tie")


if __name__ == "__main__":
    unittest.main()
