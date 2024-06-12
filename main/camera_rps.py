

import cv2
from keras.models import load_model
import numpy as np
import random

# Load the pre-trained model
model = load_model('converted_keras/keras_model.h5')
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# Class labels
class_labels = open("converted_keras/labels.txt", "r").readlines() # Example labels
def get_computer_choice():
    """
    Randomly choose between 'Rock', 'Paper', and 'Scissors' for the computer.
    """
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def get_prediction(frame):
    """
    Get the prediction from the model for a given frame.
    """
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image
    prediction = model.predict(data)
    predicted_class = class_labels[np.argmax(prediction)]
    return predicted_class

def get_winner(computer_choice, user_choice):
    """
    Determine the winner of the game based on the rules of Rock-Paper-Scissors.
    If the computer wins, return 'You lost'.
    If the user wins, return 'You won!'.
    If it's a tie, return 'It is a tie!'.
    """
    if user_choice == 'Nothing':
        return "No valid user input detected. Please try again."
    
    if computer_choice == user_choice:
        return "It is a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You won!"
    else:
        return "You lost"

def play():
    """
    Play a game of Rock-Paper-Scissors using the camera.
    """
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        flipped_frame = cv2.flip(frame, 1)
        user_choice = get_prediction(flipped_frame)
        
        # Display the frame with the user's predicted choice
        cv2.putText(flipped_frame, f'User choice: {user_choice}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', flipped_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    computer_choice = get_computer_choice()
    print(f"Computer choice: {computer_choice}")
    print(f"User choice: {user_choice}")
    
    result = get_winner(computer_choice, user_choice)
    print(result)

if __name__ == "__main__":
    play()


