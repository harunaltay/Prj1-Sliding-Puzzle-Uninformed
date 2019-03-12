import heapq


class NodeX(object):

    def __init__(self, depth):
        self.depth = depth

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
        return str(self.depth)


print("merhaba!")

n1 = NodeX(11)
n2 = NodeX(2)
n3 = NodeX(333)
n4 = NodeX(4)
n5 = NodeX(5)

# pq = [4, 3, 7, 2, 9, 1, 6]
pq = [n1, n2, n3, n4, n5]

heapq.heapify(pq)
print(pq)

n6 = NodeX(6)
heapq.heappush(pq, n6)
print(pq)

node = heapq.heappop(pq)
print(node.depth)

node = heapq.heappop(pq)
print(node.depth)

node = heapq.heappop(pq)
print(node.depth)

# b = n1.__lt__(n2)
# b = n1 < n2


