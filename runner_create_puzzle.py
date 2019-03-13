import sys

from _utility_solvability import *

if len(sys.argv) != 3:
    print("usage: python runner_create_puzzle.py solvable/unsolvable/unknown 5")
    exit(0)

puzzle_type = sys.argv[1]
print("puzzle_type:", puzzle_type)

n = sys.argv[2]
n = int(n)

matrix = ""

if puzzle_type == "solvable":
    matrix = create_a_matrix_which_is_solvable(n)

elif puzzle_type == "unsolvable":
    matrix = create_a_matrix_which_is_unsolvable(n)

elif puzzle_type == "unknown":
    matrix = create_a_random_matrix(n)

else:
    print("usage: python runner_create_puzzle.py solvable/unsolvable/unknown 5")
    exit(0)

for line in matrix:
    print(line)
