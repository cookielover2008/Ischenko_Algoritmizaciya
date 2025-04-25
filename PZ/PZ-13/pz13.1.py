# В матрице элементы третьей строки заменить элементами из одномерного
# динамического массива соответствующей размерности.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

replacement = [10, 20, 30]

if len(matrix) >= 3 and len(matrix[2]) == len(replacement):
    matrix[2] = replacement

for row in matrix:
    print(row)
