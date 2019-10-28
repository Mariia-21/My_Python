file = open(r'C:\Users\mariia.kusailo\PycharmProjects\test\test.txt') # open file
l = []
l = file.readlines()

for i in range(len(l)):
    print(l[i], end='')       # print file on screen

print()

for i in l:
    print(i, end='')
    print(len(i), 'симв. ', end='')      # print count of symbols in string
    j = i.split(' ')
    print(len(j), 'сл.')                # print count of words in line
    print()

print('Колличество строк в файле:', len(l))  # print count of lines in file