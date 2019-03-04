import time

start = time.time()
"the code you want to test stays here"

j = 0
for i in range(100000):
    j += 1
    print("*")

end = time.time()
print(end - start, "seconds")
