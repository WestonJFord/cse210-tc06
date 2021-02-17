class Player():
    '''set the move for the player'''
    
    def __init__(self):
        pass
    def test_import(self):
        print('Player')
        
    def set_code(self):
        self.player = Roster.get_current()
        self.code = Move.get_code()
        self.codes = {}
        self.codes[self.player] = self.code