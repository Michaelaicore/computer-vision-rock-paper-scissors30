"""
Rock-Paper-Scissors Game Module

This module allows the user to play a game of Rock-Paper-Scissors against the computer. 
The computer randomly selects between Rock, Paper, and Scissors, and the user is prompted 
to input their choice. The game then determines the winner based on the classic rules of 
Rock-Paper-Scissors and prints the result.

Functions:
- get_computer_choice: Randomly selects and returns 'Rock', 'Paper', or 'Scissors'.
- get_user_choice: Prompts the user for their choice and returns it.
- get_winner: Determines and prints the winner based on the choices made by the computer and the user.
- play_game: Orchestrates the game by calling the other functions and printing the choices and result.

Usage:
Run this module directly to play a game of Rock-Paper-Scissors.
"""

import random


def get_computer_choice():
    """Randomly pick an option between 'Rock', 'Paper', and 'Scissors' and return the choice."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def get_user_choice():
    """Ask the user for an input and return it."""
    user_choice = input("Please choose Rock, Paper, or Scissors: ")
    return user_choice.capitalize()


def get_winner(computer_choice, user_choice):
    """Determine the winner of the game and print the result."""
    if computer_choice == user_choice:
        print("It is a tie!")
        return "Tie"
    elif (
        (computer_choice == "Rock" and user_choice == "Scissors")
        or (computer_choice == "Scissors" and user_choice == "Paper")
        or (computer_choice == "Paper" and user_choice == "Rock")
    ):
        print("You lost")
        return "Computer"
    else:
        print("You won!")
        return "User"


def play_game():
    """Play a game of Rock, Paper, Scissors."""
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")
    get_winner(computer_choice, user_choice)


if __name__ == "__main__":
    play_game()
