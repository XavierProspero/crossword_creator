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

class Cell:

    def __init__(self, is_black, pos):
        # Local variables
        self.is_startX = False                  # bool
        self.is_startY = False                  # bool
        self.letter = None                      # string
        self.is_black = is_black                # a bool
        self.pos = pos                          # a tuple of integers
        self.parentX = None                     # None means no parent.
        self.parentY = None

# Public
    def __str__(self):
        return ("isblack: {}, pos: {}, letter: {}, isstartX {}, IsStartY {}"
            .format(self.is_black, self.pos, self.letter, self.IsStartX(), self.IsStartY()))

    def GetPosition(self):
        return self.pos

    def IsStart(self):
        return False

    def IsStartX(self):
        return self.is_startX

    def IsStartY(self):
        return self.is_startY

    def GetIsWhite(self):
        return not self.is_black

    def GetLetter(self, letter):
        return self.letter

    def SetLetter(self, letter):
        self.letter = letter

    def GetParentX(self):
        return self.parentX

    def SetParentX(self, cell):
        self.parentX = cell

    def GetParentY(self):
        return self.parentY

    def SetParentY(self, cell):
        self.parentY = cell


class StartCell(Cell):

    def __init__(self, cell):
        super(StartCell, self).__init__(cell.is_black, cell.GetPosition())

        self.wordX = None
        self.wordY = None

        self.wordXLength = 0
        self.wordYLength = 0

# Public
    def IsStart(self):
        return True

    def GetWordX(self):
        return self.wordX

    def GetWordY(self):
        return self.wordY

#Test
Cell(True, (1, 0))
