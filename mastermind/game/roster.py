class Roster():
    ''' add players to the roster
    get player
    get the current player
    and return the next player'''
    def __init__(self):
        self.roster = []
        pass
    def test_import(self):
        print('Roster')

    def add_player(self, player1, player2):
        '''add players to the roster from console'''
        self.roster = [player1, player2]
        return self.roster

    def get_current(self):
        '''get and return the current player'''
        if self.next_player() != self.roster[0]:
            return self.roster[1]
        else:
            return self.roster[0]

    def next_player(self):
        '''use current player to return the next player'''
        if self.get_current() == self.roster[0]:
            return self.roster[1]