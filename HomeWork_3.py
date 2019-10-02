# Task 1

stroka = input('Введите строку: ')
stroka = stroka.split()
lenWord = 0
maxWord = ''

for i in stroka:          # find word with maximum length
    if len(i) > lenWord:
        maxWord = i        # word with maximum length
        lenWord = len(i)   # word length
print('Самое длинное слово: %s. Длина слова: %d' % (maxWord, len(maxWord)))




# Task 2

s = input('Введите строку: ')
s = s.split()        # split string
for i in s:
    print(i, end=' ')  # print new string
