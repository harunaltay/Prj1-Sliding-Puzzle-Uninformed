import sys

from SolverDFS_Iterative_Deepening_iterative import *


def runner_iterative_deepening():
    # f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-03.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-04.txt'   # DFS bunu harika çözdü! İnanamadım! Özel seçilmiş bir durum olabilir.
    f_name = 'puzzle-text-files/puzzle3x3-05.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-07.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-01.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-unsolvable.txt'

    if len(sys.argv) != 2:
        print("usage: python runner_DFS_Iterative_Deepening.py puzzleX.txt")
        return

    f_name = sys.argv[1]
    print("file:", f_name)

    solver = SolverDFS_Iterative_Deepening_iterative()
    solver.iterative_from_file_name(f_name)


if __name__ == '__main__':
    runner_iterative_deepening()
