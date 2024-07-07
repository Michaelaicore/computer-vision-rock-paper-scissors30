"""
camera_rps.py

This module contains the RockPaperScissorsGame class, which implements a Rock-Paper-Scissors game
using computer vision. The game captures video input from a webcam, predicts hand gestures using a
pre-trained neural network model, and determines the winner of each round based on the user's and
computer's choices.

Classes:
    RockPaperScissorsGame: A class to represent and play the Rock-Paper-Scissors game.
"""


import time
import numpy as np

import cv2
from keras.models import load_model


class RockPaperScissorsGame:
    """
    A class to represent a Rock-Paper-Scissors game using computer vision.

    Attributes:
        model (keras.Model): The pre-trained model for predicting hand gestures.
        cap (cv2.VideoCapture): The video capture object for webcam input.
        class_names (list): List of class labels.
        user_wins (int): Counter for the user's wins.
        computer_wins (int): Counter for the computer's wins.

    Methods:
        preprocess_image(frame): Preprocesses the captured image for model prediction.
        get_prediction(frame): Predicts the hand gesture from the captured frame.
        countdown_and_capture(countdown_time): Displays a countdown and captures the frame.
        determine_winner(user_guess, computer_choice): Determines the winner of the round.
        display_continue_prompt(frame): Displays a prompt to continue or quit the game.
        play_round(): Conducts a single round of the game.
        run(): Runs the main game loop.
    """

    def __init__(self, model_path, labels_path):
        """
        Initializes the Rock-Paper-ScissorsGame with the given model and labels path.

        Parameters:
            model_path (str): Path to the pre-trained model.
            labels_path (str): Path to the labels file.
        """
        # Load the pre-trained model
        self.model = load_model(model_path)
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise Exception("Could not open video device")

        # Load class labels
        with open(labels_path, "r") as file:
            self.class_names = [line.strip().split(" ")[1] for line in file.readlines()]

        self.user_wins = 0
        self.computer_wins = 0

    def preprocess_image(self, frame):
        """
        Preprocesses the captured image for model prediction.

        Parameters:
            frame (numpy.ndarray): The captured frame from the webcam.

        Returns:
            numpy.ndarray: The preprocessed image ready for prediction.
        """
        img_size = (224, 224)  # Assuming the model expects 224x224 images
        frame_resized = cv2.resize(frame, img_size)
        img_array = np.array(frame_resized) / 255.0
        img_array_expanded = np.expand_dims(img_array, axis=0)
        return img_array_expanded

    def get_prediction(self, frame):
        """
        Predicts the hand gesture from the captured frame.

        Parameters:
            frame (numpy.ndarray): The captured frame from the webcam.

        Returns:
            str: The predicted label (Rock, Paper, Scissors, or Nothing).
        """
        preprocessed_image = self.preprocess_image(frame)
        predictions = self.model.predict(preprocessed_image)

        # Print the raw model prediction for debugging
        print(f"Raw model predictions: {predictions}")

        predicted_class = np.argmax(predictions[0])
        predicted_label = self.class_names[predicted_class]
        print(f"predicted_label: {predicted_label}")

        return predicted_label

    def countdown_and_capture(self, countdown_time=3):
        """
        Displays a countdown and captures the frame at the end of the countdown.

        Parameters:
            countdown_time (int): The countdown time in seconds (default is 3 seconds).

        Returns:
            tuple: The predicted label and the captured frame.
        """
        start_time = time.time()
        while True:
            ret, frame = self.cap.read()
            if not ret:
                raise Exception("Failed to capture image")

            elapsed_time = time.time() - start_time
            remaining_time = countdown_time - int(elapsed_time)

            if remaining_time <= 0:
                user_guess = self.get_prediction(frame)
                print(f"You chose: {user_guess}")
                return user_guess, frame
            else:
                cv2.putText(
                    frame,
                    f"Show your hand in: {remaining_time}",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )
                cv2.imshow("Rock Paper Scissors", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                return None, None

    def determine_winner(self, user_guess, computer_choice):
        """
        Determines the winner of the round based on user and computer choices.

        Parameters:
            user_guess (str): The user's choice (Rock, Paper, Scissors, or Nothing).
            computer_choice (str): The computer's randomly chosen move.

        Returns:
            str: The winner of the round ("user", "computer", or "tie").
        """
        if user_guess == computer_choice:
            return "tie"
        elif (
            (user_guess == "Rock" and computer_choice == "Scissors")
            or (user_guess == "Paper" and computer_choice == "Rock")
            or (user_guess == "Scissors" and computer_choice == "Paper")
        ):
            return "user"
        else:
            return "computer"

    def display_continue_prompt(self, frame):
        """
        Displays a prompt to continue or quit the game.

        Parameters:
            frame (numpy.ndarray): The frame to display the prompt on.

        Returns:
            bool: True if the user wants to continue, False if the user wants to quit.
        """
        while True:
            cv2.putText(
                frame,
                "Press 'c' to continue or 'q' to quit",
                (50, 400),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )
            cv2.imshow("Rock Paper Scissors", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("c"):
                break
            elif key == ord("q"):
                return False
        return True

    def play_round(self):
        """
        Conducts a single round of the game.

        Returns:
            bool: True if the game should continue, False if the game should end.
        """
        user_guess, frame = self.countdown_and_capture()
        if user_guess is None:
            return False

        computer_choice = np.random.choice(["Rock", "Paper", "Scissors"])
        print(f"Computer chose: {computer_choice}")

        if user_guess == "Nothing":
            print("No valid input detected. Try again.")
            return True

        winner = self.determine_winner(user_guess, computer_choice)
        if winner == "user":
            self.user_wins += 1
            print("You win this round!")
        elif winner == "computer":
            self.computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(f"Score - You: {self.user_wins}, Computer: {self.computer_wins}")

        if self.user_wins == 3:
            print("Congratulations! You won the game!")
            return False
        elif self.computer_wins == 3:
            print("Sorry, the computer won the game.")
            return False

        return self.display_continue_prompt(frame)

    def run(self):
        """
        Runs the main game loop.
        """
        try:
            while self.user_wins < 3 and self.computer_wins < 3:
                if not self.play_round():
                    break
        finally:
            self.cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    model_path = "converted_keras/keras_model.h5"
    labels_path = "converted_keras/labels.txt"

    game = RockPaperScissorsGame(model_path, labels_path)
    game.run()
