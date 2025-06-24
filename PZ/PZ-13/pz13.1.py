# В матрице элементы третьей строки заменить элементами из одномерного
# динамического массива соответствующей размерности.

import random
n = input("Введите размер матрицы: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправилно ввели!")
        n = input("Введите размер матрицы: ")
matrix = [[random.randint(1, 50) for el in range(n)] for s in range(n)]
print("Ваша матрица: ")
for row in matrix:
    print(row)

replacement = [random.randint(1, 50) for el in range(n)]

if len(matrix[2]) == len(replacement):
    matrix[2] = replacement

print("Меняем третью строчку на ", replacement)
for row in matrix:
    print(row)
