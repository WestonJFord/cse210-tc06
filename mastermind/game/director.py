#Weston Ford
#CSE 210 Adam Hayes
#Unit 6

#imports
from .board import Board
from .console import Console
from .move import Move
from .player import Player
from .roster import Roster


class Director:
    def __init__(self):     #initialized all the classes        
        self.board = Board()
        self.console = Console()
        self.move = Move(1) #I guess Zach put the parameters in his __init__ so I'd actually have to initialize it every time.
        self.player = Player()
        self.roster = Roster()

    def test_import(self):  #Making sure I can import, initialize, and call everyone's classes without issues
        self.board.test_import()
        self.console.test_import()
        self.move.test_import()
        self.player.test_import()
        self.roster.test_import()

    def start_game(self):   #not sure what I'm supposed to do here if only one other person actually filled out their classes...
        player1 = console.get_name()