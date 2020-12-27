import sys
from solver import Solver
from utils import print_debug

if len(sys.argv) < 3:
    raise AssertionError('An input file and an output file name must be provided.')
input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

solver = Solver(input_file)
solver.SaveResults(output_file)