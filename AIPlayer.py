#
# AI Player for use in Connect Four  
#

import random  
from connect_four import *

class AIPlayer(Player):
    """ an intelligent computer player"""
    def __init__(self, checker, tiebreak, lookahead):
        """ AIPlayer has two new attributes while others are inherited from Player"""
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """ returns a string representing an AIPlayer object"""
        s = self.tiebreak + ', ' + str(self.lookahead)
        c = super().__repr__()
        c += ' ' + '(' + s + ')'
        return c
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board
        and that returns the index of the column with the maximum score"""
        m = max(scores)
        index = []
        for i in range(len(scores)):
            if scores[i] == m:
                index += [i]
        if self.tiebreak == 'LEFT':
            return index[0]
        elif self.tiebreak == 'RIGHT':
            return index[-1]
        else:
            return random.choice(index)
    
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores for the columns in b"""
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(b)
                scores[col] = 100 - max(opp_scores)
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ overrides the next_move method that is inherited from Player
        return the called AIPlayer‘s judgment of its best possible move"""
        self.num_moves += 1    
        best = self.max_score_column(self.scores_for(b))
        return best
    
    
    
    
    
    
    
    
    
                
