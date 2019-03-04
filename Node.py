from Board import *


class Node(object):

    def __init__(self, board, parent):
        self.board = board
        self.node_parent = parent
        self.nodes_children = []


def test_stub_node_basic():
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

    board = Board(matrix)

    node = Node(board, None)

    print("vector:", node.board.vector)


if __name__ == '__main__':
    test_stub_node_basic()

