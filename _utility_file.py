from _utility_matrix_vector import *


def create_a_vector_and_a_matrix_from_a_text_file(file_name):
    vector = create_a_vector_from_a_text_file(file_name)
    matrix = create_a_matrix_from_a_list(vector)
    return vector, matrix


def create_a_vector_from_a_text_file(file_name):
    f = open(file_name, 'r+')

    first_line = f.readline().strip()
    n = int(first_line)
    # print(n)

    vector_all = []

    for i in range(n):
        line = f.readline().strip()
        # print(line)
        vector_of_the_line = line.split()
        # print(vector_of_the_line)
        for j in range(n):
            string = vector_of_the_line[j]
            # print(string)
            integer = int(string)
            # print(integer)
            vector_all.append(integer)

    # print("vector:", vector_all)

    f.close()
    return vector_all


# __main__ ----------------------------------------------------------------

if __name__ == '__main__':
    f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    f_name = 'puzzle-text-files/puzzle4x4-00.txt'

    # vector = create_a_vector_from_a_text_file(f_name)

    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(f_name)
    print(vector)
    for line in matrix:
        print(line)


# -------------------------------------------
# for line in open("puzzle-text-files/puzzle2x2-00.txt"):
#     print(line, end='')

# -------------------------------------------
# with open('puzzle-text-files/puzzle2x2-00.txt', encoding='utf8') as fp:
#     for line in fp:
#         print(line.strip())
