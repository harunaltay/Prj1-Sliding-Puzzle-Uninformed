from _utility_matrix_vector import *


# class --------------------------------------------------------------------

class Board:
    """ game board with tiles on it, the blocks """
    BoardCount = 0

    def __init__(self, blocks):
        self.n = len(blocks)
        self.blocks = blocks


# TODO: Board cTor : Board(matrix, n)
#       n lazım mı?


# test stubs ---------------------------------------------------------------

def test_stub_basic_demo():
    n = 3
    # matrix = create_a_matrix_with_zeros(n)
    matrix = create_a_matrix_solution(n)
    board1 = Board(matrix)
    print("n:", board1.n)
    for line in board1.blocks:
        print(line)
    vector = make_list_the_matrix_into_one_list(matrix)
    print("vector:", vector)
    matrix = make_a_matrix_from_a_list(vector)
    print("matrix again")
    for line in matrix:
        print(line)


def main():
    print("Merhaba main() method")
    print("__name__ : ", __name__)
    print("__file__ : ", __file__)


# __main__ ----------------------------------------------------------------

if __name__ == '__main__':
    test_stub_basic_demo()

