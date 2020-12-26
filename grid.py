"""
    The grid in which the crossword puzzle resides.
    Assumes grid is N x N.

    A well formatted grid file looks like.

    3
    w w w
    w b w
    w w w
"""
from cell import Cell, StartCell
from utils import print_info, print_debug

class Grid:

    def __init__(self, file):
        # Create empty cells
        self.__init_grid_from_file(file)
        self.__find_starting_words()

# Public
    def GetCell(self, x, y):
        if x >= self.N or y >= self.N:
            return None
        return self.grid[y][x]

    def GetCellRight(self, cell):
        # Returns the cell to the right of cell.
        return self.GetCell(cell.pos[1] + 1, cell.pos[0])

    def GetCellDown(self, cell):
        # Returns the cell to the left of cell.
        return self.GetCell(cell.pos[1], cell.pos[0] + 1)

    def SetWord(self, word, start_cell, step):
        # step is Step struct
        # Do some sanity checks.
        if (
                (step is STEP_RIGHT and not start_cell.IsStartX())
                or (step is STEP_DOWN and not start_cell.IsStartY())
            ):
            print_info("SetWord() called on non starting cell!")
            return

        # Handle case of setting word in X.
        if step is STEP_RIGHT:
            # FIXME

        else if step is STEP_DOWN:
            # FIXME
        else:
            print_info("SetWord(): wtf is step: {} {}".format(step.x, step.y))

    def FindConstraint(self, start_cell, step):
        # FIXME

    def ClearWord(self, start_cell, step):
        # FIXME


# Private
    def __str__(self):
        for row in self.grid:
            for cell in row:
                print(cell)
            print()
        return ""

    def __init_grid_from_file(self, file):
        BLACK = ["b", "b\n"]
        WHITE = ["w", "w\n"]

        print_info("reading file named: {}".format(file))

        with open(file, 'r') as f:
            lines = f.readlines()
            print_debug(lines)
            N = int(lines[0])

            if N is not (len(lines) - 1):
                print_info("init_grid_from_file: received malformed crossword file.")
            else:
                self.grid = [[[] for _ in range(N)] for _ in range(N)]
                self.N = N

                for line_idx, line in enumerate(lines[1:]):

                    characters = line.split(" ")

                    if len(characters) is not N:
                        print_info("init_grid_from_file: received malformed crossword file.")
                    else:
                        for c_idx, c in enumerate(characters):
                            is_black = (c in BLACK)
                            pos = (line_idx, c_idx)
                            self.grid[line_idx][c_idx] = Cell(is_black, pos)

        print_info("succesfully read file: {}".format(file))
        print_info("puzzle: {}".format(self.grid))


    def __find_starting_words(self):
        # Go through the grid and find where words start.
        # There is a maximum of two words starting at a square.
        # Read right to left.
        # DGAF if it's slow.

        for rowIdx, row in enumerate(self.grid):

            for colIdx, cell in enumerate(row):

                cur_cell = cell

                if cur_cell.GetIsWhite():
                    # See if it's a parent in X
                    if (
                            (cur_cell.GetParentX() is None)
                            # and (print(self.GetCellRight(cur_cell)) or True)
                            and (self.GetCellRight(cur_cell) is not None)
                            and self.GetCellRight(cur_cell).GetIsWhite()
                        ):

                        # Looks like this cell is a new father...
                        if not cell.IsStart():
                            new_cell = StartCell(cur_cell)
                            self.grid[rowIdx][colIdx] = new_cell

                        cur_cell = self.grid[rowIdx][colIdx]
                        cur_cell.SetParentX(cur_cell)
                        cur_cell.is_startX = True

                        # Count down to see when this word ends
                        next_cell = self.GetCellRight(cur_cell)

                        idx = 0
                        for _ in range(colIdx, self.N - 1):
                            if next_cell.GetIsWhite():
                                next_cell.SetParentX(cur_cell)
                                next_cell = self.GetCellRight(next_cell)
                                idx += 1
                            else:
                                break

                        new_cell.wordXLength = idx
                    # See if it's a parent in Y
                    if (
                            (cur_cell.GetParentY() is None)
                            and (self.GetCellDown(cur_cell) is not None)
                            and self.GetCellDown(cur_cell).GetIsWhite()
                        ):
                        # Looks like this cell is a new father...
                        if not cur_cell.IsStart():
                            new_cell = StartCell(cur_cell)
                            self.grid[rowIdx][colIdx] = new_cell

                        cur_cell = self.grid[rowIdx][colIdx]
                        cur_cell.SetParentY(cur_cell)
                        cur_cell.is_startY = True

                        # Count down to see when this word ends
                        next_cell = self.GetCellDown(cur_cell)

                        idx = 0
                        for _ in range(rowIdx, self.N - 1):
                            if next_cell.GetIsWhite():
                                next_cell.SetParentY(cur_cell)
                                next_cell = self.GetCellDown(next_cell)
                                idx += 1
                            else:
                                break

                        new_cell.wordYLength = idx

# Test
grid = Grid("test4.puzzle")
print()
print_debug(grid)
