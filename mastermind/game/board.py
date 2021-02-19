import random

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

    def to_string(self, roster, player_one_move, player_two_move) -> str:
        """
            convert board data to a string
            Returns: a string
        """
        board_string = "\n--------------------"
        board_string += (
            f"\nPlayer {roster.roster[0].get_name()}:{player_one_move.get_guess()}, {player_one_move.check_code()}"
        )
        board_string += (
            f"\nPlayer {roster.roster[1].get_name()}:{player_two_move.get_guess()}, {player_two_move.check_code()}"
        )

        board_string += "\n--------------------"
        return board_string

    def _prepare(self):
        """
        sets up the board with a random set of 4 digits
        """
        # Build board
        for _ in range(4):
            self.numbers_to_guess.append(str(random.randint(1, 9)))
        self.numbers_to_guess = ''.join(self.numbers_to_guess)