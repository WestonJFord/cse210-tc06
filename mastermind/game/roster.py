class Roster():
    ''' add players to the roster
    get player
    get the current player
    and return the next player'''
    def __init__(self):
        self.current = 0
        self.roster = []

    def test_import(self):
        print('Roster')

    def add_player(self, player1, player2):
        '''add players to the roster from console'''
        self.roster = [player1, player2]
        return self.roster

    def get_current(self):
        '''get and return the current player'''
        return self.roster[self.current]

    def next_player(self):
        '''use current player to return the next player'''
        self.current = (self.current + 1) % len(self.roster)