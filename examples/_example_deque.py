from collections import deque


class Person(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


ali = Person("Ali", "111")
mike = Person("Mike", "222")
john = Person("John", "333")

queue = deque()

queue.append(ali)
queue.append(mike)
queue.append(john)

popped = queue.popleft()
print(popped)
print(popped.name)
print(popped.phone)

