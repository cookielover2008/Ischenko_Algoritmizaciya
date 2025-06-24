# В матрице найти среднее арифметическое положительных элементов

import random
n = input("Введите размер матрицы: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправилно ввели!")
        n = input("Введите размер матрицы: ")
matrix = [[random.randint(-50, 50) for el in range(n)] for s in range(n)]
print("Ваша матрица: ")
for row in matrix:
    print(row)

positive_elements = []

for row in matrix:
    for el in row:
        if el > 0:
            positive_elements.append(el)

if positive_elements:
    ura = sum(positive_elements) / len(positive_elements)
    print("Среднее арифметическое положительных элементов: ", ura)
else:
    print("Положительных элементов в матрице нет.")
