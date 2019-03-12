import heapq

pq = [5, 2, 6, 8, 0, 1, 2, 4]

heapq.heapify(pq)

print(pq)

heapq.heappush(pq, 7)

print(pq)

number = heapq.heappop(pq)
print(number)

number = heapq.heappop(pq)
print(number)

number = heapq.heappop(pq)
print(number)
