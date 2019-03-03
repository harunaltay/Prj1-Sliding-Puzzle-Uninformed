w, h = 10, 5

Vector = [x for x in range(w)]

print(Vector)

Matrix = [[0 for x in range(w)] for y in range(h)]
Matrix = [[x + y*w + 1 for x in range(w)] for y in range(h)]
Matrix[h-1][w-1] = 0

print(Matrix)

for line in Matrix:
    print(line)

