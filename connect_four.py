from Board import Board
from Player import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """ takes two parameters: a Player object p for the player whose move is being processed
    and a Board object b for the board on which the game is being played
    it perform all of the steps involved in processing a single move by player p on board b"""
    turn = str(p) + "'s turn"
    print(turn)
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    print()
    if b.is_win_for(p.checker) == True:
        r = str(p) + ' wins in ' + str(p.num_moves) + ' moves.' + '\n' + 'Congratulations!' 
        print(r)
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    """ an unintelligent computer player that chooses at random from the available columns"""
    
    def next_move(self, b):
        """overrides the next_move method that is inherited from Player
        this version of next_move should choose at random from the columns in the board b
        that are not yet full, and return the index of that randomly selected column"""
        self.num_moves += 1
        index = []
        for i in range(b.width):
            if b.can_add_to(i):
                index += [i]
        r = random.choice(index)
        return r

























    
    
