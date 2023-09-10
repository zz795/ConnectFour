class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        """ contructs a new Board object"""
        self.height = height
        self.width = width
        self.slots = [[' ']* self.width for r in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''
        for row in range(self.height):
            s += '|'
            count = 1
            for col in range(self.width):
                s += self.slots[row][col] + '|'
                count += 2
            s += '\n'
        for col in range(len(s[0:count])):
            s += '-'
        s += '\n'
        for x in range(self.width):
            s += ' ' + str(x%10)   
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        row = 0
        while self.slots[row][col] == ' ':
            if row == self.height-1:
                self.slots[row][col] = checker
                break
            elif self.slots[row+1][col] == 'X' or self.slots[row+1][col] == 'O':
                self.slots[row][col] = checker
                break
            else:
                row += 1
    
    def reset(self):
        """ resert the Board object so that all slots recontain space characters"""
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '

    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if the column number is valid
        otherwise return False"""
        if col >= 0 and col <= self.width-1:
            if self.slots[0][col] == ' ':
                    return True
            else:
                return False
        else:
            return False
    
    def is_full(self):
        """ returns True if the called Board object is completely full of checkers
        otherwise returns False"""
        for c in range(self.width):
            if self.slots[0][c] == ' ':
                return False
        return True

    def remove_checker(self, col):
        """ removes the top checker from column col of the Board ojbect"""
        for r in range(self.height):
            if self.slots[r][col] == 'X' or self.slots[r][col] == 'O':
                self.slots[r][col] = ' '
                break

    def is_win_for(self, checker):
        """ input checker is either 'X' or 'O'
        returns True if there are four consecutive slots containing checker on the board
        otherwise return False"""
        assert(checker == 'X' or checker == 'O')
        # horinzontally
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                    return True
        # vertically
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                        return True
        # diagonally up from left to right
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                    return True
        # diagonally up from right to left
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col + 3] == checker and \
                    self.slots[row + 1][col + 2] == checker and \
                    self.slots[row + 2][col + 1] == checker and \
                    self.slots[row + 3][col] == checker:
                    return True
        # if none of them wins
        return False
