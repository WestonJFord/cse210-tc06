#Weston Ford
#CSE 210 Adam Hayes
#Unit 6

class Director:
    def __init__(self):
        from .board import Board
        self.board = Board()
        from .console import Console
        self.console = Console()
        from .move import Move
        self.move = Move()
        from .player import Player
        self.player = Player()
        from .roster import Roster
        self.roster = Roster()

    def test_import(self):
        self.board.test_import()
        self.console.test_import()
        self.move.test_import()
        self.player.test_import()
        self.roster.test_import()

    def start_game(self):
        pass