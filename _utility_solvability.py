from _utility_inversion import *
from _utility_matrix_vector import *


def row_of_blank_square(matrix):
    n = len(matrix)
    row = -1
    for i in range(n):
        for j in range(n):
            x = matrix[i][j]
            if x == 0:
                row = i
            # print(x, end=' ')
        # print()
    # print("row:", row)
    return row


def is_this_matrix_solvable(matrix):
    n = len(matrix)
    vector = create_a_list_from_a_matrix(matrix)
    number_of_inversions = the_number_of_inversion_in_a_list_of_integers(vector)
    answer = False
    if n % 2 == 1:
        # if n is odd -> if number of inversions is even -> solvable
        # print("n is odd")
        if number_of_inversions % 2 == 0:
            # print("solvable")
            answer = True
        else:
            pass
            # print("unsolvable")
    else:
        # if n is even -> if number of inversions + row of the blank square is odd -> solvable
        # print("n is even")
        row_number = row_of_blank_square(matrix)
        # print("row_number:", row_number)
        invariant = number_of_inversions + row_number
        # print("invariant:", invariant)
        if invariant % 2 == 1:
            # print("solvable")
            answer = True
        else:
            pass
            # print("un-solvable")
    return answer


def interchange_two_tiles(matrix):
    vector = create_a_list_from_a_matrix(matrix)
    length = len(vector)

    x = -1
    y = -1

    for i in range(length - 1):
        x = vector[i]
        if x == 0:
            continue

        for j in range(i + 1, length):
            y = vector[j]
            if y == 0:
                continue
            temp = vector[i]
            vector[i] = vector[j]
            vector[j] = temp

            matrix = create_a_matrix_from_a_list(vector)
            return matrix


def create_a_matrix_which_is_solvable(n):
    matrix = create_a_random_matrix(n)
    is_solvable = is_this_matrix_solvable(matrix)
    if is_solvable:
        return matrix
    else:
        matrix = interchange_two_tiles(matrix)
        return matrix


def create_a_matrix_which_is_unsolvable(n):
    matrix = create_a_random_matrix(n)
    is_solvable = is_this_matrix_solvable(matrix)
    if not is_solvable:
        return matrix
    else:
        matrix = interchange_two_tiles(matrix)
        return matrix


# test stubs ----------------------------------------------------------------------------


def test_stub_solvable_matrix():
    n = 4
    matrix = create_a_matrix_which_is_solvable(n)
    answer = is_this_matrix_solvable(matrix)
    print("is solvable:", answer)


def test_stub_unsolvable_matrix():
    n = 4
    matrix = create_a_matrix_which_is_unsolvable(n)
    answer = is_this_matrix_solvable(matrix)
    print("is solvable:", answer)


def test_stub_solvable_file():
    # f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-00.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-02.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-01.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-03.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-01.txt'
    f_name = 'puzzle-text-files/puzzle4x4-unsolvable.txt'

    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(f_name)
    answer = is_this_matrix_solvable(matrix)
    print("is solvable:", answer)


if __name__ == '__main__':
    test_stub_unsolvable_matrix()
