# Variant 1
import math

def figure(a):

    def cirkl():
        r = int(input("Введите радиус: "))
        s = math.pi * r * r
        return 'Площадь круга', s

    def square():
        a = int(input("Введите сторону а: "))
        b = int(input("Введите сторону b: "))
        s = a * b
        return 'Площадь квадрата', s

    def triangle():
        a = int(input("Введите сторону а: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите сторону c: "))
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return 'Площадь треугольника', s

    if a == 'c':
        return cirkl()
    elif a == 's':
       return square()
    elif a == 't':
       return triangle()


a = input("Введите фигуру: ")
fig, squ = figure(a)

print(fig, squ)




# Variant 2
import math

def cirkle():             # Function for calculating the area of a circle
    r = int(input("Введите радиус: "))
    s = math.pi * r * r
    return s


def square():             # Function for calculating the area of a square
    a = int(input("Введите сторону а: "))
    b = int(input("Введите сторону b: "))
    s = a * b
    return s


def triangle():          # Function for calculating the area of a triangle
    a = int(input("Введите сторону а: "))
    b = int(input("Введите сторону b: "))
    c = int(input("Введите сторону c: "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def rezult(func):
    return func()

tempCirkle = cirkle
tempSquare = square
temptriangle = triangle

a = input("Введите фигуру: ")

if a == 'c':
    print('Площадь круга:', rezult(tempCirkle))
elif a == 's':
    print('Площадь квадрата:', rezult(tempSquare))
elif a == 't':
    print('Площадь треугольника:', rezult(temptriangle))
