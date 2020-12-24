"""
The grid is made of cells.
Some cells are starts of words.

All indexing is row column.

Use Public functions to manipulate cell.
"""
from dataclasses import dataclass

@dataclass
class Step:
    x: int
    y: int

class Cell:

    def __init__(self, is_black, pos):
        # Local variables
        self.is_start = False
        self.letter = None
        self.is_black = is_black
        self.pos = pos

# Public
    def __str__(self):
        return "isblack: {}, pos: {}, letter: {}".format(self.is_black, self.pos, self.letter)

    def GetIsBlack(self):
        return self.is_black

    def GetLetter(self, letter):
        return self.letter

    def SetLetter(self, letter):
        self.letter = letter


class StartCell(Cell):

    def __init__(self, cell):

        #  These are Steps
        self.next_letterX = None
        self.next_letterY = None

        self.wordX = None
        self.wordY = None

# Public
    def GetNumWords(self):
        retval = 0

        if self.next_letterX:
            retval += 1
        if self.next_letterY:
            retval += 1

        return retval

    def GetWord(self):
        return word

#Test
Cell(True, (1, 0))
