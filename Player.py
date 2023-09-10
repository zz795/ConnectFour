from Board import Board

class Player:
    """ a new data type represent a player in Connect Four game
    """
    def __init__(self, checker):
        """ constructs a new Player object"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object"""
        s = 'Player'
        s += ' ' + str(self.checker)
        return s
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player object’s opponent"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """ accepts a Board object b as a parameter
        returns the column where the player wants to make the next move"""
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')
        
        
