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

STEP_RIGHT = Step(1,  0)
STEP_DOWN  = Step(0, -1)

@dataclass
class Parents:
    x: Cell
    y: Cell

class Cell:

    def __init__(self, is_black, pos):
        # Local variables
        self.is_start = False
        self.letter = None
        self.is_black = is_black
        self.pos = pos
        self.parents = Parents(None, None)

# Public
    def __str__(self):
        return "isblack: {}, pos: {}, letter: {}".format(self.is_black, self.pos, self.letter)

    def GetIsStart(self):
        return self.is_start

    def GetIsBlack(self):
        return self.is_black

    def GetLetter(self, letter):
        return self.letter

    def SetLetter(self, letter):
        self.letter = letter

    def GetParentX(self):
        return self.parents.x

    def SetParentX(self, cell):
        self.parents.x = cell

    def GetParentY(self):
        return self.parents.y

    def SetParentY(self, cell):
        self.parents.y = cell


class StartCell(Cell):

    def __init__(self, cell):

        self.is_start = True

        #  These are Steps
        self.next_letterX = Step(0, 0)
        self.next_letterY = Step(0, 0)

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
