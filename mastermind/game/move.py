
class Move():
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _code (integer): The players secret code.
    """

    def __init__(self, code):
        """THe class constructor.
        
        Args:
            self (Move): an instance of Move.
            code (integer): the players secret code.
        """
        
        self._code = code

    def test_import(self):
        print('Move')

    def get_code(self):
        """Returns the code.
        
        Arge:      
            self (move): an instance of Move."""
        
        return self._code