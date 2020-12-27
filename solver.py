"""
    The meat and potatos. Where the magic happens.
    Uses some shitty variant of a back tracking search to
    find a satisfactory set of words.
"""
from grid import Grid
from utils import print_info, print_debug
from dictionary import Smart_Dictionary
from cell import STEP_RIGHT, STEP_DOWN


class Solver:

    def __init__(self, file_name):

        self._grid = Grid(file_name)
        self._dictionary = Smart_Dictionary()

# Public
    def SaveResults(self, output_file):
        self._grid.write_grid(output_file)

    def BacktrackingSearch(self):
        pass

    def solve1(self):
        num_starting_cells = len(self._grid._starting_words)

        idx = 0

        while idx < num_starting_cells and idx >= 0:
            cell = self._grid._starting_words[idx]

            if cell.IsStartX():
                self._grid.ClearWord(cell, STEP_RIGHT)                                      # Clear the word.
                constraint = self._grid.FindConstraint(cell, STEP_RIGHT)                    # Find the constraint
                word = self._dictionary.pop_constrained_word(len(constraint), constraint)   # Query dictionary

                if word is not None:
                    self._grid.SetWord(word, cell, STEP_RIGHT)                              # Set the word
                else:
                    idx -= 1                                                                # Backtrack
                    continue

            if cell.IsStartY():
                self._grid.ClearWord(cell, STEP_DOWN)                                       # Clear the word.
                constraint = self._grid.FindConstraint(cell, STEP_DOWN)                     # Find the constraint
                word = self._dictionary.pop_constrained_word(len(constraint), constraint)   # Query dictionary

                if word is not None:
                    self._grid.SetWord(word, cell, STEP_DOWN)                               # Set the word
                else:
                    idx -= 1                                                                # Backtrack
                    continue

            idx += 1

        if idx < 0:
            print_info("Solver.solve1: There is no initial word.")

# Private
    def __recursive_backtracking(self, grid):
        pass


# Test
if __name__ == "__main__":
    solver = Solver("test8.puzzle")

    solver.solve1()

    solver._grid.write_grid("test.txt")
