f = open('nehirler.txt', 'r+')

# r : read only
# w : write only
# a : append
# r+ : read/write

# content = f.read()
# print(content)

# f.write("nil")

# for line in f:
#     print(line)

# lines = f.readlines()
# for line in lines:
#     print(line)

with open('nehirler.txt', encoding='utf8') as fp:
    for line in fp:
        print('-', line.strip(), '-')

f.close()

# for line in open("myfile.txt"):
#     print(line, end='')
