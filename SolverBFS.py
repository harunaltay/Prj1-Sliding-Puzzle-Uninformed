from Solver import *
from Board import *
from collections import deque
import time


class SolverBFS (Solver):

    def __init__(self, matrix):
        super().__init__(matrix)
        self.queue = deque()

    def solve(self):
        print("solving begins ... in Solver_BFS ...")

        self.queue.append(self.node_initial)

        counter_loop = 0
        conter_number_of_nodes_expanded = 0
        counter_number_of_nodes_appended = 0

        while True:
            counter_loop += 1
            node_popped = self.queue.popleft()
            # print("popped from the fringe:", node_popped.board.matrix)

            # print("aşağıdaki matrisler fringe'ye append ediliyor ...")

            if is_this_matrix_one_of__the_solutions(node_popped.board.matrix):
                print()
                print("*** bulundu:", node_popped.board.matrix)
                print("counter_loop:", counter_loop)
                print("counter_number_of_nodes_appended:", counter_number_of_nodes_appended)
                print()
                answer_list = []
                node_iter =node_popped
                while True:
                    matrix = node_iter.board.matrix
                    answer_list.append(matrix)
                    if node_iter.node_parent is None:
                        answer_list.reverse()
                        return answer_list
                    node_iter = node_iter.node_parent

            # conter_number_of_nodes_expanded += 1 - yanlış oldu

            # bu child grand_parent ile aynıysa, geç, continue ...
            board_list = node_popped.board.get_neighbors()
            same = True
            for board_item in board_list:
                if node_popped.node_parent is not None:
                    for i in range(self.n):
                        for j in range(self.n):
                            if board_item.matrix[i][j] != node_popped.node_parent.board.matrix[i][j]:
                                same = False
                                break
                        if not same:
                            break
                else:
                    same = False
                if same:
                    continue

                counter_number_of_nodes_appended += 1

                # bu child'i append et ...
                node_new = Node(board_item, node_popped)
                self.queue.append(node_new)
                # for line in board_item.matrix:
                #     print(line)
                # print()

            # print(counter_loop, "loop ----------------------------------------------------------------------------")
            if counter_loop == 1000000:
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

    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(f_name)

    print(vector)
    for line in matrix:
        print(line)

    solver = SolverBFS(matrix)

    if not solver.is_solvable:
        print("this puzzle is not solvable... program terminates...")
        return

    start = time.time()

    answer_list = solver.solve()

    end = time.time()
    print("solved in", end - start, "seconds")

    print("the number of steps to the solution:", len(answer_list) - 1)
    print()
    print("****************************************************************************************")

    for matrix in answer_list:
        for line in matrix:
            print(line)
        print()

    print("****************************************************************************************")


if __name__ == '__main__':
    test_stub_solver_bfs_main()
