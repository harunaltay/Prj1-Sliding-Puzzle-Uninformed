from Node import *
from collections import deque


class Solver:

    def __init__(self, matrix):

        self.queue = deque()
        self.stack = []

        self.limit = -1

        self.n = len(matrix)
        self.matrix_initial = matrix
        self.is_solvable = is_this_matrix_solvable(matrix)

        self.board_initial = Board(matrix)
        self.node_initial = Node(self.board_initial, None)

        self.solution_list_of_matrixes = []

        self.solution_matrix = create_a_matrix_solution(self.n)
        self.solution_vector = create_a_vector_from_a_matrix(self.solution_matrix)

        self.time_start = 0
        self.time_stop = 0
        self.time_elapsed = 0

        self.message_short = ""
        self.message_long = ""

        self.answer_list = []

        self.counter_loop = 0  # as well, number_of_nodes_expanded, extracted from the fringe
        self.counter_number_of_nodes_appended = 0

    def report_to_string(self):
        s = ""

        s += "**************************************************\n"
        s += "*** Solution found!\n"
        s += "The number of moves/steps to the solution: " + str(len(self.answer_list) - 1) + " moves.\n"
        s += "time_elapsed: " + str(self.time_elapsed) + "\n"
        s += "message_short: " + self.message_short + "\n"
        s += "message_long: " + self.message_long + "\n"
        s += "counter_loop (number of expanded/extracted from the fringe nodes): " + str(self.counter_loop) + "\n"
        s += "counter_number_of_nodes_appended: " + str(self.counter_number_of_nodes_appended) + "\n"
        s += "\n"
        s += "Starting from the given/initial puzzle, ends with the goal.\n"
        s += "\n"

        step = 0
        for matrix in self.answer_list:
            s += "move: " + str(step) + "\n\n"
            for line in matrix:
                s += str(line) + "\n"
            s += "\n"
            step += 1

        s += "***************************************************\n"

        return s


if __name__ == '__main__':
    print("This is an abstract class!!! Dont run it! Run one of its descendants.")
