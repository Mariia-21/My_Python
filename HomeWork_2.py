try:
    h = int(input('Введите высоту треугольника:')) # variable for hight triangle
    i = 1  # variable for count
    w = 1  # variable for width triangle
    if h != 0:
        while i <= h:
            print((h - i) * ' ', (w * '^'))    # printing triangle
            i += 1
            w += 2
    else:
        print('Высота треугольника не может быть 0')
except:
    print('Высота треугольника не может быть пустой!')