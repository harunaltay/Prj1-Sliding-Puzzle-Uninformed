from _utility_file import *


def the_number_of_inversion_in_a_list_of_integers(vector):
    number_of_inversions = 0
    length = len(vector)

    for i in range(length - 1):
        x = vector[i]
        if x == 0:
            continue
        # print(x, "- ", end="")

        for j in range(i + 1, length):
            y = vector[j]
            if y == 0:
                continue
            # print(y, end=' ')
            if x > y:
                number_of_inversions += 1
        # print()
    # print("inv", number_of_inversions)
    return number_of_inversions


# test stubs ---------------------------------------------


def test_stub_the_number_of_inversions():
    # f_name = 'puzzle-text-files/puzzle2x2-00.txt'
    # f_name = 'puzzle-text-files/puzzle4x4-00.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-02.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-01.txt'
    # f_name = 'puzzle-text-files/puzzle2x2-03.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-00.txt'
    # f_name = 'puzzle-text-files/puzzle3x3-31.txt'
    f_name = 'puzzle-text-files/puzzle3x3-unsolvable.txt'

    vector, matrix = create_a_vector_and_a_matrix_from_a_text_file(f_name)
    number_of_inversions = the_number_of_inversion_in_a_list_of_integers(vector)
    print("the number of inversion", number_of_inversions)


# TODO: "MAIN" bu satır konutundan çalışır hale getirilecek, en sonunda
#       bunun gibi, bütün ilgili dosyalara main metodu eklenecek

def main_inversion():
    pass


if __name__ == '__main__':
    test_stub_the_number_of_inversions()


# for i in range(len(vector)):
#     print(i, vector[i])
