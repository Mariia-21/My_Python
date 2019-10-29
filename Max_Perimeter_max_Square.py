import geometric_Figures


figuresList = []

for i in range(3):
    choice = input("Введите фигуру: ")

    if choice == 'c':
        figure = geometric_Figures.Circle(float(input("Введите радиус: ")))

    elif choice == 's':
        l = float(input("Введите сторону а: "))
        w = float(input("Введите сторону b: "))
        figure = geometric_Figures.Rectangle(l, w)

    elif choice == 't':
        AB = float(input("Введите сторону а: "))
        BC = float(input("Введите сторону b: "))
        CD = float(input("Введите сторону c: "))
        figure = geometric_Figures.Triangle(AB, BC, CD)

    figuresList.append(figure)

parameter = int(input("1 - Максимальная площадь\n2 - Максимальный периметр "))
maxS = 0
figureName = 0
parameterName = ''


for i in figuresList:
    if parameter == 1:
        s = i.getSquare()
        parameterName = 'Максимальная площадь = '
    else:
        s = i.getPerimeter()
        parameterName = 'Максимальный периметр = '
    if maxS < s:
        maxS = s
        figureName = i


print(parameterName, maxS)
print("Параметры фигуры: ")
for keys, values in figureName.__dict__.items():
    print(keys, '-', values)

