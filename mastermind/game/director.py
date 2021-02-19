#Weston Ford
#CSE 210 Adam Hayes
#Unit 6

from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _board (Board): An instance of the class of objects known as Board.
        _console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        code: the code for the game
        _moves (Move): Instances of the class of objects known as Move.
        _roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self.keep_playing = True
        
        self.code = self._board.numbers_to_guess

        self._moves = [Move(self.code, '----'), Move(self.code, '----')]
        self._roster = Roster()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self.keep_playing:
            self.print_board()
            self.turn()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        player = [None, None]
        for n in range(2):
            name = self._console.get_name()
            player[n] = Player(name)
        self._roster.add_player(player[0], player[1])
    
    def print_board(self):
        """Outputs the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        board = self._board.to_string(self._roster, self._moves[0], self._moves[1])
        self._console.write(board)


    def turn(self):
        """Gets input from player, applies input, checks to see if player won, selects next player

        Args:
            self (Director): An instance of Director.
        """
        # get player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your guess? ")
        self._moves[self._roster.current].update_guess(guess)
        player.set_move(self._moves[self._roster.current])

        # check for victory
        if str(guess) == str(self.code):
            self._console.write(f'\n{player.get_name()} won!')
            self.keep_playing = False

        # next player
        self._roster.next_player()