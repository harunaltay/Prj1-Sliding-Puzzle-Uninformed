from _utility_matrix_vector import *
from _utility_file import *
from _utility_solvability import *
from Node import *


class Solver:

    def __init__(self, matrix):
        self.n = len(matrix)
        self.matrix_initial = matrix
        self.is_solvable = is_this_matrix_solvable(matrix)

        self.board_initial = Board(matrix)
        self.node_initial = Node(self.board_initial, None)

        self.solution_list_of_matrixes = []

        self.solution_matrix = create_a_matrix_solution(self.n)
        self.solution_vector = create_a_vector_from_a_matrix(self.solution_matrix)

    def solve(self):
        s = "solving ... in Solver ..."
        return s


def test_stub_solver_main():
    # f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'
    f_name = 'puzzle-text-files/puzzle4x4-01.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-unsolvable.txt'

    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(f_name)

    print(vector)
    for line in matrix:
        print(line)

    solver = Solver(matrix)

    if not solver.is_solvable:
        print("this puzzle is not solvable... program terminates...")
        return

    s = solver.solve()

    print(s)
    print("solution vector:", solver.solution_vector)


if __name__ == '__main__':
    test_stub_solver_main()

