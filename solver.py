"""
    The meat and potatos. Where the magic happens.
    Uses some shitty variant of a back tracking search to
    find a satisfactory set of words.
"""
from grid import Grid
from dictionary import Smart_Dictionary
from utils import print_debug, print_info

class Solver:

    def __init__(self, file_name):

        self._grid = Grid(file_name)
        self._dictionary = Smart_Dictionary()

# Public
    def SaveResults(self, output_file):
        self._grid.write_grid("test.txt")

    def BacktrackingSearch(self):
        pass

# Private
    def __recursive_backtracking(self, grid):
        pass 