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

# Public

# Private
    def __init_grid_from_file(self, file):
        BLACK = "b"
        WHITE = "w"

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
                            is_black = (c is BLACK)
                            pos = (line_idx, c_idx)
                            self.grid[line_idx][c_idx] = Cell(is_black, pos)

        print_info("succesfully read file: {}".format(file))
        print_info("puzzle: {}".format(self.grid))


# Test
Grid("test.puzzle")
