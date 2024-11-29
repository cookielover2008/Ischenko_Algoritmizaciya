# Используя четыре вызова функции Minmax, найти минимальное и максимальное из данных чисел A, B, C, D.
a = input('Введи число A: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input("Введи A заново: ")
b = input('Введи число B: ')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели!')
        b = input("Введи B заново: ")
c = input('Введи число C: ')
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Неправильно ввели!')
        c = input("Введи C заново: ")
d = input('Введи число D: ')
while type(d) != int:
    try:
        d = int(d)
    except ValueError:
        print('Неправильно ввели!')
        d = input("Введи D заново: ")

def Minmax(X, Y):
    if X < Y:
        return X, Y
    else:
        return Y, X

min1, max1 = Minmax(a, b)  # Минимум и максимум для A и B
min2, max2 = Minmax(c, d)  # Минимум и максимум для C и D
samoe_minimalnoe, zub_dayu = Minmax(min1, min2)  # Минимум из двух минимальных значений
zub_dayu, samoe_maximalnoe = Minmax(max1, max2)  # Максимум из двух максимальных значений

print('Минимальное число: ', samoe_minimalnoe)
print('Максимальное число: ', samoe_maximalnoe)
