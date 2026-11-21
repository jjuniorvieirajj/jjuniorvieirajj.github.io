import unittest

from game import determine_winner


class DetermineWinnerTest(unittest.TestCase):
    def test_equal_choices_are_ties(self):
        cases = ("rock", "paper", "scissors")

        for choice in cases:
            with self.subTest(choice=choice):
                self.assertEqual(determine_winner(choice, choice), "It's a tie!")

    def test_user_winning_matchups(self):
        cases = (
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper"),
        )

        for user_choice, computer_choice in cases:
            with self.subTest(
                user_choice=user_choice,
                computer_choice=computer_choice,
            ):
                self.assertEqual(
                    determine_winner(user_choice, computer_choice),
                    "You win!",
                )

    def test_computer_winning_matchups(self):
        cases = (
            ("scissors", "rock"),
            ("rock", "paper"),
            ("paper", "scissors"),
        )

        for user_choice, computer_choice in cases:
            with self.subTest(
                user_choice=user_choice,
                computer_choice=computer_choice,
            ):
                self.assertEqual(
                    determine_winner(user_choice, computer_choice),
                    "Computer wins!",
                )


if __name__ == "__main__":
    unittest.main()
