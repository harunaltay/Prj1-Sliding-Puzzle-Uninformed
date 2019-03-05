from _utility_file import create_a_vector_and_a_matrix_from_a_text_file


def are_two_matrices_the_same(matrix1, matrix2):
    n = len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True


def test_stub_and_example_for_matrix_equivalence():
    f_name1 = 'puzzle-text-files/puzzle3x3-03.txt'
    # f_name2 = 'puzzle-text-files/puzzle3x3-03.txt'
    f_name2 = 'puzzle-text-files/puzzle3x3-05.txt'

    vector1, matrix1 = create_a_vector_and_a_matrix_from_a_text_file(f_name1)
    vector2, matrix2 = create_a_vector_and_a_matrix_from_a_text_file(f_name2)

    n = len(matrix1)

    print("n:", n)
    print("vector1:", vector1)
    print("vector2:", vector2)

    # ------------------------------------------------------------------

    same_matrices = True
    inner_loop_broken_once = False

    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[i][j]:
                same_matrices = False
                inner_loop_broken_once = True
                break
        if inner_loop_broken_once:
            break

    print()
    print("same_matrices", same_matrices)
    print("inner_loop_broken_once", inner_loop_broken_once)

    # ------------------------------------------------------------

    answer = are_two_matrices_the_same(matrix1, matrix2)

    print()
    print("answer:", answer)

