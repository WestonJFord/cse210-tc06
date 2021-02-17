import random


class Board:
    """Handles the board and all of it's requisite variables"""

    def __init__(self):
        self._piles = []
        self._prepare()

    def apply(self, move):
        """
        applies move to surface of board
        removes a number of stones from the pile
        attr: move an instance of Move
        Returns:
        """
        pile = move.get_pile()
        stones = move.get_stones()
        try:
            self._piles[pile] = self._piles[pile][: stones * -2]
        except IndexError:
            print("That row does not exist or have that many stones")

    def is_empty(self):
        """
        determines if _piles is empty
        Returns:
            True if pile is empty
            false if pile isn't empty
        """

        # if row is empty remove it from the object
        emptyRows = 0

        for pile in self._piles:
            if len(pile) == 0:
                emptyRows += 1

        if emptyRows == len(self._piles):
            return True

        return False

    def to_string(self):
        """
        convert board data to a string
        Returns: a string
        """
        board_string = "--------------------"
        for i in range(0, len(self._piles)):
            new_row = f"\n{i}: {self._piles[i]}"
            board_string += new_row

        board_string += "\n--------------------"
        return board_string

    def _prepare(self):
        """
        sets up the board with a random number of piles and a random number of stones in each pile
        """
        # Build board
        for _ in range(random.randint(2, 5)):
            self._piles.append("0 " * random.randint(1, 9))