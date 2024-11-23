def Minmax(X, Y):
    if X < Y:
        return X, Y
    else:
        return Y, X


a = input('Введи число A: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
b = input('Введи число B: ')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели!')
c = input('Введи число C: ')
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Неправильно ввели!')
d = input('Введи число D: ')
while type(d) != int:
    try:
        d = int(d)
    except ValueError:
        print('Неправильно ввели!')
min_value, max_value = Minmax(a, b)
min_value, max_value = Minmax(min_value, c)
min_value, max_value = Minmax(min_value, d)
print('Максимальное число: ', max_value)
print('Минимальное число: ', min_value)
