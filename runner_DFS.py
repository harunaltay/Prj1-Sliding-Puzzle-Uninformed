import sys

from SolverDFS_iterative import *


# print("sys.argv      :", str(sys.argv))
# print("len(sys.argv) :", len(sys.argv))


def runner_solver_dfs_main_from_file():
    # f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-00.txt'
    f_name = 'puzzle-text-files/puzzle3x3-03.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-04.txt'   # DFS bunu harika çözdü! İnanamadım! Özel seçilmiş bir durum olabilir.
    # f_name = 'puzzle-text-files/puzzle3x3-05.txt' # loop 1.000.000 aşıyor
    # f_name = 'puzzle-text-files/puzzle4x4-07.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-01.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-unsolvable.txt'

    if len(sys.argv) != 2:
        print("usage: python runner_DFS.py puzzleX.txt")
        return

    f_name = sys.argv[1]
    print("file:", f_name)

    runner_solver_dfs_main_from_file_name(f_name)


def runner_solver_dfs_main():
    # f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-00.txt'
    f_name = 'puzzle-text-files/puzzle3x3-03.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-04.txt'   # DFS bunu harika çözdü! İnanamadım! Özel seçilmiş bir durum olabilir.
    # f_name = 'puzzle-text-files/puzzle3x3-05.txt' # loop 1.000.000 aşıyor
    # f_name = 'puzzle-text-files/puzzle4x4-07.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-01.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-unsolvable.txt'

    runner_solver_dfs_main_from_file_name(f_name)


def runner_solver_dfs_main_from_file_name(file_name):
    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(file_name)

    runner_solver_dfs_main_from_the_matrix(matrix)


def runner_solver_dfs_main_from_the_matrix(matrix):

    print("here is the puzzle ..")
    print()

    for line in matrix:
        print(line)

    print()

    solver = SolverDFS_iterative(matrix)

    if not solver.is_solvable:
        print("this puzzle is not solvable... method returns...")
        return

    answer_list, message_short, message_long, time_elapsed = solver.tree_search_DFS_iterative()

    s = solver.report_to_string()
    print(s)


if __name__ == '__main__':
    runner_solver_dfs_main_from_file()
