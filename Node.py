from Board import *


class Node(object):

    def __init__(self, board, parent):
        self.board = board
        self.node_parent = parent
        self.nodes_children = []

        self.depth = -1         # Koçum be! Bu lazım olacak: Depth Limited, Iterative Deepening! ...
        # Lazım oldu şimdi. Uniform Cost'ta -> path_cost = depth !

        self.step_cost = 0      # Russell & Norvig 3.rd ed page 79
        self.path_cost = 0      # Russell & Norvig 3.rd ed page 79 - Uniform_Cost'ta kullanılacak.

        self.state = ""         # Russell & Norvig 3.rd ed page 79, 82 -> explored, expanded?, what else?
        self.explored = False   # Bu da benden olsun :-)
        self.expanded = False   # Bu dahi benden -> DFS'de bunu kullanacağım! Öyle görünüyor :-)
        self.terminated = False # Ölmüşleri de istersen bir yerde tut! Graph-Search de lazım oluyormuş galiba!
                                # Benim terminated dediğime, aşağıdaki discovered demiş galiba.
        self.visited = False    # Bi de bu çıktı! Bu bizle ilgili değil sanırım. Var olan bir tree için sanırım.
        self.discovered = False # mark DISCOVERED only after popping the vertex, not before pushig it! Bakınız (*)
                                # (*) https://www.techiedelight.com/depth-first-search/
                                # Bu discovered'i GRAPH için kullanıyor. Bizim işimiz TREE ile.

    def __eq__(self, other):
        return self.depth == other.depth

    def __lt__(self, other):
        return self.depth < other.depth

    def __gt__(self, other):
        return self.depth > other.depth

    def __le__(self, other):
        return self.depth <= other.depth

    def __ge__(self, other):
        return self.depth >= other.depth

    def __ne__(self, other):
        return self.depth != other.depth

    def __repr__(self):
        return "depth: " + str(self.depth)  # böyle kalsın. gerçekte, faydalı olması için, ...
        # ... vector veya matrisi de yazdırman lazım. bu şimdi sadece debug maksatlı.


# explored : ? : Herhalde: Buldun, frontiere push/append ettin. İşte o!
# expanded : frontierden pop/remove ettin, çocuklarını frontiere push/append ettin. işte expand ettin.


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

