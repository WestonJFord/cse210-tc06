
class Move():
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _code (integer): The players secret code.
    """

    def __init__(self, code, guess):
        """The class constructor.
        
        Args:
            self (Move): an instance of Move.
            code (integer): the players secret code.
        """
        
        self._code = code
        self._guess = guess

    def get_code(self):
        """Returns the code.
        
        Args:      
            self (move): an instance of Move."""
        
        return self._code

    def get_guess(self):
        """Returns the guess.
        
        Args:
            self (move): an instance of Move."""

        return self._guess
    
    def update_guess(self, guess):
        self._guess = guess

    def check_code(self):
        """Checks the guess against the code and returns a validation string.
        
        Args:
            self (move): an instance of Move."""
        
        validation = ['-', '-', '-', '-']
        code = str(self._code)
        guess = str(self._guess)
        
        # Checks to see if the each digit in the guess is in the code.
        # If it is, then it will put a 'O', if not, then '*'.
        index = 0
        for digit in guess:
            if digit in code:
                validation[index] = 'O'
                index += 1
            else:
                validation[index] = '*'
                index += 1
        
        # Checks to see if the digit is in the right number
        # in the right place.
        index = 0
        while index < 4:
            if guess[index] == code[index]:
                validation[index] = 'X'
                index += 1
            else:
                index += 1

        # Converts the list into a string.
        return_str = ''
        for string in validation:
            return_str += string
        
        return return_str
