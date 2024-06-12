
import unittest
from unittest.mock import patch
import sys
import os

# Add the path to the computer-vision-rock-paper-scissors30 directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'computer-vision-rock-paper-scissors30')))

from main.manual_rps import get_computer_choice, get_user_choice, get_winner

class TestRockPaperScissors(unittest.TestCase):
    """Unit tests for the Rock-Paper-Scissors game."""

    def test_get_computer_choice(self):
        """Test that the computer's choice is one of 'Rock', 'Paper', or 'Scissors'."""
        choices = ["Rock", "Paper", "Scissors"]
        for _ in range(100):  # Run multiple times to check randomness
            choice = get_computer_choice()
            self.assertIn(choice, choices)

    @patch('builtins.input', return_value='rock')
    def test_get_user_choice_rock(self, mock_input):
        """Test that the user's choice is correctly returned as 'Rock'."""
        self.assertEqual(get_user_choice(), 'Rock')

    @patch('builtins.input', return_value='paper')
    def test_get_user_choice_paper(self, mock_input):
        """Test that the user's choice is correctly returned as 'Paper'."""
        self.assertEqual(get_user_choice(), 'Paper')

    @patch('builtins.input', return_value='scissors')
    def test_get_user_choice_scissors(self, mock_input):
        """Test that the user's choice is correctly returned as 'Scissors'."""
        self.assertEqual(get_user_choice(), 'Scissors')

    def test_get_winner_tie(self):
        """Test that the game correctly identifies a tie."""
        self.assertEqual(get_winner('Rock', 'Rock'), 'Tie')
        self.assertEqual(get_winner('Paper', 'Paper'), 'Tie')
        self.assertEqual(get_winner('Scissors', 'Scissors'), 'Tie')

    def test_get_winner_computer(self):
        """Test that the game correctly identifies when the computer wins."""
        self.assertEqual(get_winner('Rock', 'Scissors'), 'Computer')
        self.assertEqual(get_winner('Scissors', 'Paper'), 'Computer')
        self.assertEqual(get_winner('Paper', 'Rock'), 'Computer')

    def test_get_winner_user(self):
        """Test that the game correctly identifies when the user wins."""
        self.assertEqual(get_winner('Scissors', 'Rock'), 'User')
        self.assertEqual(get_winner('Paper', 'Scissors'), 'User')
        self.assertEqual(get_winner('Rock', 'Paper'), 'User')

if __name__ == '__main__':
    unittest.main()









# import unittest
# from unittest.mock import patch
# import sys, os
# # Add the path to the computer-vision-rock-paper-scissors30 directory
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'computer-vision-rock-paper-scissors30')))
# from manual_rps import get_computer_choice, get_user_choice, get_winner


# class TestRockPaperScissors(unittest.TestCase):
#     """Unit tests for the Rock-Paper-Scissors game."""

#     def test_get_computer_choice(self):
#         """Test that the computer's choice is one of 'Rock', 'Paper', or 'Scissors'."""
#         choices = ["Rock", "Paper", "Scissors"]
#         for _ in range(100):  # Run multiple times to check randomness
#             choice = get_computer_choice()
#             self.assertIn(choice, choices)

#     @patch('builtins.input', return_value='rock')
#     def test_get_user_choice_rock(self, mock_input):
#         """Test that the user's choice is correctly returned as 'Rock'."""
#         self.assertEqual(get_user_choice(), 'Rock')

#     @patch('builtins.input', return_value='paper')
#     def test_get_user_choice_paper(self, mock_input):
#         """Test that the user's choice is correctly returned as 'Paper'."""
#         self.assertEqual(get_user_choice(), 'Paper')

#     @patch('builtins.input', return_value='scissors')
#     def test_get_user_choice_scissors(self, mock_input):
#         """Test that the user's choice is correctly returned as 'Scissors'."""
#         self.assertEqual(get_user_choice(), 'Scissors')

#     def test_get_winner_tie(self):
#         """Test that the game correctly identifies a tie."""
#         self.assertEqual(get_winner('Rock', 'Rock'), 'Tie')
#         self.assertEqual(get_winner('Paper', 'Paper'), 'Tie')
#         self.assertEqual(get_winner('Scissors', 'Scissors'), 'Tie')

#     def test_get_winner_computer(self):
#         """Test that the game correctly identifies when the computer wins."""
#         self.assertEqual(get_winner('Rock', 'Scissors'), 'Computer')
#         self.assertEqual(get_winner('Scissors', 'Paper'), 'Computer')
#         self.assertEqual(get_winner('Paper', 'Rock'), 'Computer')

#     def test_get_winner_user(self):
#         """Test that the game correctly identifies when the user wins."""
#         self.assertEqual(get_winner('Scissors', 'Rock'), 'User')
#         self.assertEqual(get_winner('Paper', 'Scissors'), 'User')
#         self.assertEqual(get_winner('Rock', 'Paper'), 'User')

# if __name__ == '__main__':
#     unittest.main()