import random

from mastermind.game import roster


class Board:
    """Handles the board and all of it's requisite variables"""

    def __init__(self):
        self.numbers_to_guess = []
        self._prepare()

    def is_guessed(self, guess):
        """
        applies move to surface of board
        removes a number of stones from the pile
        attr: move an instance of Move
        Returns:
        """
        _guess = guess.get_guess()
        for i in range(4):
            if _guess[i] != self.numbers_to_guess[i]:
                return False

        # Only called if all numbers return true
        return True

    def check_guess(self, guess):
        """
        determines if _piles is empty
        Returns:
            True if pile is empty
            false if pile isn't empty
        """

        # if row is empty remove it from the object
        correct_guesses = 0

        if not guess:
            return "----"

        for _ in self.numbers_to_guess:
            correct_guesses += 1

        guess_string = ""
        for i in range(correct_guesses):
            guess_string += "x"
        for i in range(4 - correct_guesses):
            guess_string += "o"
        return guess_string

    def to_string(self):
        """
        convert board data to a string
        Returns: a string
        """
        board_string = "--------------------"
        board_string += f"\nPlayer {roster.getCurrent}: {roster.player1_guess[-1]}, {self.check_guess(roster.player1_guess)}"
        board_string += f"\nPlayer {roster.player2}: {roster.player1_guess[-1]}, {self.check_guess(roster.player2_guess)}"

        board_string += "\n--------------------"
        return board_string

    def _prepare(self):
        """
        sets up the board with a random set of 4 digits
        """
        # Build board
        for _ in range(4):
            self.numbers_to_guess.append(random.randint(1, 9))