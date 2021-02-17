import random

class Console:
    """A code template for a computer console. The responsibility of this
    class of objects is to get text or numerical input and display text output.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """

    def __init__(self):
        self.player_num = 1

    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args:
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def get_name(self) -> str:
        '''
        asks player for their name and returns it
        Args:
            self (Screen): An instance of Screen.
        Returns: name of player
        '''
        name = input(f"Enter a name for player {self.player_num}: ")
        return name

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args:
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        return int(input(prompt))

    def write(self, text):
        """Displays the given text on the screen.

        Args:
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)