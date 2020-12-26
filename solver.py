"""
    The meat and potatos. Where the magic happens.
    Uses some shitty variant of a back tracking search to
    find a satisfactory set of words.
"""
import grid
import dictionary

class Solver:

    def __init__(self, file_name):

        self._grid = Grid(file_name)
        self._dictionary = Smart_Dictionary()

# Public

# Private
