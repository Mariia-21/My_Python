
def readMass(path):        # Function for reading massiv from file
    file = open(path)
    N = 0
    mass = []
    for line in file:
        z = []
        row = line.strip().split('  ')
        for i in range(len(row)):
            z.append(int(row[i]))
        mass.append(z)
        N += 1
    file.close()
    return mass, N


def printMass(mass, N):  # Function for printing massiv on screen
    for i in range(N):
        for j in range(N):
            print("%6d" % mass[i][j], end='')
        print()


def summRow(mass, N):   # Function for calculating sum of a column
    j = 0
    mass1 = []
    while j < N:
        summ = 0
        for i in range(N):
            summ += mass[i][j]
        mass1.append(summ)
        j += 1
    return mass1


def maxSumm(mass, N):  # Function for found max summ and column
    maxS = mass[0]
    num = 0
    for i in range(N):
        if mass[i] > maxS:
            maxS = mass[i]
            num = i + 1
    return maxS, num


mass, N = readMass('C:\\Users\\mariia.kusailo\\PycharmProjects\\test\\file_2.txt')

printMass(mass, N)

print('-------------------------------------------------------------')

rez = summRow(mass, N)

for i in range(N):
    print("%6d" % rez[i], end='')      # print column totals list
print()

print('-------------------------------------------------------------')

maxSumma, column = maxSumm(rez, N)

print('Максимальная сумма', maxSumma, 'находится в столбце', column)







