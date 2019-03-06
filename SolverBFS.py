from _utility_matrix_equality import are_two_matrices_the_same
from _utility_Solver import trace_to_the_initial_node_from_the_solution_node_iterative
from Solver import *
from Board import *
from collections import deque
import time


class SolverBFS (Solver):

    def __init__(self, matrix):
        super().__init__(matrix)

    # Solves the puzzle
    def tree_search_BFS(self):
        self.time_start = time.time()

        if not self.is_solvable:
            print("The puzzle is not a solvable puzzle. Check it before calling this method. halting.")
            raise Exception('The puzzle is not a solvable puzzle. Check it before calling this method. halting.')

        # print("solving begins ... in Solver_BFS ...")

        self.queue.append(self.node_initial)

        # turns until finds one of the optimal solutions
        # assumes that the puzzle has a solution.. see: "solver.is_solvable" attribute of Solver
        while True:
            self.counter_loop += 1

            # IF THE FRONTIER IS EMPTY ...
            # THEN RETURN FAILURE

            if len(self.queue) == 0:
                # print("failure : queue/frontier/fringe is empty.. no solution found! .. returns.")
                self.message_short = "failure.. no solution.."
                self.message_long = "failure : queue/frontier/fringe is empty.. no solution found! .. returns."
                self.time_elapsed = 0
                return self.answer_list, self.message_short, self.message_long, self.time_elapsed

            # CHOOSE A LEAF NODE AND ...
            # REMOVE IT FROM THE FRONTIER

            # Choose the shallowest node from the frontier
            # print("popped from the queue/frontier/fringe:", node_popped.board.matrix)
            node_popped = self.queue.popleft()

            # IF THE NODE CONTAINS A GOAL STATE ...
            # THEN RETURN THE CORRESPONDING SOLUTION

            # pop ettiğimiz node, bir çözüm node'si mi?
            if is_this_matrix_one_of__the_solutions(node_popped.board.matrix):
                # print("*** !!! BULUNDU !!! :", node_popped.board.matrix)
                self.answer_list = \
                    trace_to_the_initial_node_from_the_solution_node_iterative(node_popped)
                self.time_stop = time.time()
                self.time_elapsed = self.time_stop - self.time_start

                return self.answer_list, \
                       self.message_short, \
                       self.message_long, \
                       self.time_elapsed

            # pop edilen node 'bir solution' değilmiş...
            # ... öyleyse bu node'yi patlat, expand et, ...
            # ... sonra da fringe'ye append et, grand-parent'i ile aynı olan node hariç.

            # "EXPAND" THE CHOOSEN NODE, ...
            # ADDING THE RESULTING NODES TO THE FRONTIER

            board_list_neighbors = node_popped.board.get_neighbors()

            # generate edilen her bir yeni node'yi fringe'ye append et...
            # ... tabi, grand-parent'i ile aynı olan birisi hariç
            for board_item in board_list_neighbors:

                # bu child grand_parent ile aynıysa, geç, continue ...
                if node_popped.node_parent is not None:
                    is_child_and_grand_parent_same = \
                        are_two_matrices_the_same\
                            (board_item.matrix, node_popped.node_parent.board.matrix)
                    if is_child_and_grand_parent_same:
                        continue

                self.counter_number_of_nodes_appended += 1

                # bu child'i append et ...
                # aha bu nodu EXPLORE ettik! Artık yaşıyo! Galiba öyle oldu. Hadi hayırlısı.
                node_new = Node(board_item, node_popped)
                self.queue.append(node_new)
                # for line in board_item.matrix:
                #     print(line)
                # print()

            # print(counter_loop, "loop ---------------------------------------------------------")
            # garanti olsun diye. yine de 1.000.000 loop gerektirecek puzzle olur mu bilmem. Olursa bakarız.
            if self.counter_loop == 1000000:
                print("loop 1.000.000 oldu. Çalışma kesildi.")
                break


def test_stub_solver_bfs_main():
    # f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-03.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-05.txt'
    f_name = 'puzzle-text-files/puzzle4x4-07.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-01.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-unsolvable.txt'

    test_stub_solver_bfs_main_from_file_name(f_name)


def test_stub_solver_bfs_main_from_file_name(file_name):
    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(file_name)

    test_stub_solver_bfs_main_from_the_matrix(matrix)


def test_stub_solver_bfs_main_from_the_matrix(matrix):
    for line in matrix:
        print(line)

    print()

    solver = SolverBFS(matrix)

    if not solver.is_solvable:
        print("this puzzle is not solvable... method returns...")
        return

    answer_list, message_short, message_long, time_elapsed = solver.tree_search_BFS()

    s = solver.report_to_string()
    print(s)


if __name__ == '__main__':
    test_stub_solver_bfs_main()
