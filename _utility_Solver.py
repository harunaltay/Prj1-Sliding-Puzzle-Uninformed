

def trace_to_the_initial_node_from_the_solution_node(node_iter):
    answer_list = []

    while True:
        matrix = node_iter.board.matrix
        answer_list.append(matrix)
        if node_iter.node_parent is None:
            answer_list.reverse()
            break
        node_iter = node_iter.node_parent

    return answer_list

