s = ' '


def convertToBinarySystem(n):  # function for converting number to binary system
    global s
    if n == 1:
        s = '0001'
    if n == 2:
        s = '0010'
    if n == 3:
        s = '0011'
    if n == 4:
        s = '0100'
    if n == 5:
        s = '0101'
    if n == 6:
        s = '0110'
    if n == 7:
        s = '0111'
    if n == 8:
        s = '1000'
    if n == 9:
        s = '1001'
    return s          # function result


i = 1

while i > 0:          # not ending cycle
    try:
        n = int(input('Введите десятичное число: '))        # input user value

        if n == 0:
            print("Вы ввели число", n)
            break                                           # exit from program
        elif 1 <= n <= 9:
            s = convertToBinarySystem(n)                    # call function
            print("Число", n, "в двоичной системе: ", s)    # print result
        else:
            print("Вы ввели не десятичное число! Попробуйте еще раз! ")

    except:
        print('Вы ввели не десятичное число! Попробуйте еще раз!')
