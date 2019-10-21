goods = {'Товар 1': {1: 'Монитор', 2: 20, 3: '4500 грн'},
         'Товар 2': {1: 'Принтер', 2: 10, 3: '2500 грн'},
         'Товар 3': {1: 'Клавиатура', 2: 15, 3: '500 грн'},
         'Товар 4': {1: 'Ноутбук', 2: 4, 3: '15000 грн'},
         'Товар 5': {1: 'Наушники', 2: 17, 3: '300 грн'}
         }  # creation dictionary with all goods


def printAllGoods():                  # function for printing all goods
    for key, product in goods.items():
        print(key)
        for attribute, value in product.items():
            print('{} : {}'.format(attribute, value))


printAllGoods()

i = 1

while i > 0:           # not ending cycle

    num = input('Введите номер товара который вы хотите изменить: ')  #
    if int(num) == 0:
        printAllGoods()
        break         # exit from program
    tmp = 'Товар ' + num
    count = input('Введите новое количество: ')

    for key, product in goods.items():
        if key == tmp:
            for attribute, value in product.items():
                product.update({2: count})       # updating count of selected goods