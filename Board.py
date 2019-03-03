from typing import List
import random
import math


# matrix & vector operations ---------------------------------------------------------


def create_a_matrix_with_zeros(n):
    Matrix: List[List[int]] = [[0 for x in range(n)] for y in range(n)]
    return Matrix


def create_a_matrix_solution(n):
    Matrix = [[x + y * n + 1 for x in range(n)] for y in range(n)]
    Matrix[n - 1][n - 1] = 0
    return Matrix


def create_a_random_matrix(n):
    matrix = create_a_matrix_solution(n)
    vector = make_list_the_matrix_into_one_list(matrix)
    random.shuffle(vector)
    matrix: List[List[int]] = make_a_matrix_from_a_list(vector)
    return matrix


def make_a_matrix_from_a_list(vector):
    length = len(vector)
    n = int(math.sqrt(length))
    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[j][i] = vector[i + j*n]
            # how did this happened? :-)
    return matrix


def make_list_the_matrix_into_one_list(matrix):
    vector = []
    for line in matrix:
        for tile in line:
            vector.append(tile)
    return vector


def is_this_matrix_one_of__the_solutions(matrix):
    vector = make_list_the_matrix_into_one_list(matrix)
    answer = is_this_list_monotone_increasing_one_by_one(vector)
    return answer


def is_this_list_monotone_increasing_one_by_one(vector):
    answer = True
    for i in range(len(vector)-1):
        if vector[i] != i+1:
            answer = False
            break
    if vector[len(vector)-1] != 0:
        answer = False
    return answer


# class --------------------------------------------------------------------

class Board:
    """ game board with tiles on it, the blocks """
    BoardCount = 0

    def __init__(self, blocks):
        self.n = len(blocks)
        self.blocks = blocks

# test stubs ---------------------------------------------------------------

def test_stub():
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


def test_stub_create_a_random_matrix(n):
    matrix = create_a_random_matrix(n)
    for line in matrix:
        print(line)


def test_stub_is_this_list_monontone(n):
    matrix = create_a_matrix_solution(n)
    matrix = create_a_random_matrix(n)
    vector = make_list_the_matrix_into_one_list(matrix)
    answer = is_this_list_monotone_increasing_one_by_one(vector)
    print(answer)
    print("vector:", vector)


def test_stub_is_this_matrix_one_of_the_solutions(n):
    matrix = create_a_matrix_solution(n)
    matrix = create_a_random_matrix(n)
    answer = is_this_matrix_one_of__the_solutions(matrix)
    print(answer)
    for line in matrix:
        print(line)


def main():
    print("Merhaba main() method")
    print("__name__ : ", __name__)
    print("__file__ : ", __file__)


# __main__ ----------------------------------------------------------------


if __name__ == '__main__':
    test_stub_is_this_matrix_one_of_the_solutions(3)

# TODO: Eldeki kucuk kucuk programciklari, dosyalari elden gecir..
#       X_examples, Y_Operations, baska?

# TODO: read the matrix from a text file

# TODO: is this matrix solvable?
#       what is the number of inversion of this vector?
#       for odd n?
#       for even n?
#       find and read those 2 places in slayts
#       search in internet
#       is there code in internet finds the number od inversions?

# TODO: matrix operations:
#       make practice
#       practice: w, h... i, j... row, column...

# TODO: module?
#       package?
#       what else?

# TODO: Board -> Board_Base
#       Board_DFS, Board_BFS?, Others?

# TODO: Organize all the 6 projects into one PyCharm project ?!
#       Is tis possible? How?


