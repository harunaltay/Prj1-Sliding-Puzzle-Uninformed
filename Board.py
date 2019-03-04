from _utility_matrix_vector import *
from _utility_file import *
from _utility_solvability import *
from copy import deepcopy


# static functions --------------------------------------------------------


# class --------------------------------------------------------------------

class Board:
    """ game board with tiles on it, the blocks """
    BoardCount = 0

    def __init__(self, matrix):
        self.n = len(matrix)
        self.blocks = matrix
        self.vector = create_a_list_from_a_matrix(matrix)
        self.k_of_zero = -1
        self.i_of_zero = -1
        self.j_of_zero = -1

        for k in range(len(self.vector)):
            if self.vector[k] == 0:
                self.k_of_zero = k
                break

        found = False
        for i in range(self.n):
            for j in range(self.n):
                if self.blocks[i][j] == 0:
                    self.i_of_zero = i
                    self.j_of_zero = j
                    found = True
                    break
            if found:
                break

    def get_neighbors(self):
        neighbors = []
        if self.i_of_zero != 0:
            blocks_new = deepcopy(self.blocks)
            value_to_move = self.blocks[self.i_of_zero - 1][self.j_of_zero]
            blocks_new[self.i_of_zero][self.j_of_zero] = value_to_move
            blocks_new[self.i_of_zero - 1][self.j_of_zero] = 0
            board_new = Board(blocks_new)
            neighbors.append(board_new)

        if self.i_of_zero != self.n - 1:
            blocks_new = deepcopy(self.blocks)
            value_to_move = self.blocks[self.i_of_zero + 1][self.j_of_zero]
            blocks_new[self.i_of_zero][self.j_of_zero] = value_to_move
            blocks_new[self.i_of_zero + 1][self.j_of_zero] = 0
            board_new = Board(blocks_new)
            neighbors.append(board_new)

        if self.j_of_zero != 0:
            blocks_new = deepcopy(self.blocks)
            value_to_move = self.blocks[self.i_of_zero][self.j_of_zero - 1]
            blocks_new[self.i_of_zero][self.j_of_zero] = value_to_move
            blocks_new[self.i_of_zero][self.j_of_zero - 1] = 0
            board_new = Board(blocks_new)
            neighbors.append(board_new)

        if self.j_of_zero != self.n - 1:
            blocks_new = deepcopy(self.blocks)
            value_to_move = self.blocks[self.i_of_zero][self.j_of_zero + 1]
            blocks_new[self.i_of_zero][self.j_of_zero] = value_to_move
            blocks_new[self.i_of_zero][self.j_of_zero + 1] = 0
            board_new = Board(blocks_new)
            neighbors.append(board_new)

        return neighbors


def test_stub_board_basic_demo():
    n = 3
    matrix = create_a_matrix_solution(n)
    board = Board(matrix)
    print("n:", board.n)
    for line in board.blocks:
        print(line)


# ---------------------------------------------------------------------------


def create_board_from_a_file(file_name):
    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(file_name)
    print(vector)
    print(matrix)
    solvable = is_this_matrix_solvable(matrix)
    print(solvable)
    board = Board(matrix)
    return board


def test_stub_create_board_from_a_file():
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-01.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-unsolvable.txt'
    f_name = 'puzzle-text-files/puzzle2x2-02.txt'

    board = create_board_from_a_file(f_name)
    for line in board.blocks:
        print(line)

    print("k_of_zero:", board.k_of_zero)
    print("i_of_zero:", board.i_of_zero)
    print("j_of_zero:", board.j_of_zero)

    print("board_new ---------------------------------")
    neighbors = board.get_neighbors()

    for board_single in neighbors:
        for line in board_single.blocks:
            print(line)
        print()


# main ---------------------------------------------------------------

def main():
    print("Merhaba main() method")
    print("__name__ : ", __name__)
    print("__file__ : ", __file__)


# __main__ ----------------------------------------------------------------

if __name__ == '__main__':
    test_stub_create_board_from_a_file()
    # test_stub_board_basic_demo()
