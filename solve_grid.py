import sys
from solver import Solver
from grid import Grid
from utils import print_debug

if len(sys.argv) < 2:
    raise AssertionError('A puzzle file must be provided.')
puzzle_file = str(sys.argv[1])


grid = Grid(puzzle_file)

