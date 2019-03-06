from SolverDFS_Depth_Limited_iterative import *
from Board import *
from _utility_file import *


class SolverDFS_Iterative_Deepening_iterative():

    def __init__(self):
        pass

    def iterative_from_file_name(self, file_name):
        vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(file_name)
        solvable = is_this_matrix_solvable(matrix)
        if not solvable:
            print("unsolvable puzzle ...")
            return

        self.iterative_from_the_matrix(matrix)

    def iterative_from_the_matrix(self, matrix):
        solvable = is_this_matrix_solvable(matrix)
        if not solvable:
            print("unsolvable puzzle ...")
            return

        self.iterative_solver(matrix)

    def iterative_solver(self, matrix):

        print("puzzle to solve")
        for line in matrix:
            print(line)

        print("\nstarts solving ..\n")

        solver = SolverDFS_Depth_Limited_iterative(matrix)

        limit = 0

        while True:
            limit += 1
            if limit == 100:
                print("limit = 100 .. Bu kadar yeter.. bulamadı.. terminates..")
                return
            answer_list, message_short, message_long, time_elapsed = \
                solver.tree_search_DFS_Depth_Limited_iterative(limit)
            length = len(answer_list)
            print("limit:", limit)
            print("length of the solution list:", length)
            print()
            if length != 0:
                break

        s = solver.report_to_string()
        print(s)


def iterative_main():
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

    solver = SolverDFS_Iterative_Deepening_iterative()
    solver.iterative_from_file_name(f_name)


if __name__ == '__main__':
    iterative_main()
