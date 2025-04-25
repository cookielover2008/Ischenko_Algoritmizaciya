# В матрице найти среднее арифметическое положительных элементов

matrix = [
    [1, -2, 3],
    [4, -5, 6],
    [-7, 8, 9]
]

positive_elements = []

for row in matrix:
    for element in row:
        if element > 0:
            positive_elements.append(element)

if positive_elements:
    mean = sum(positive_elements) / len(positive_elements)
    print(f"Среднее арифметическое положительных элементов: {mean}")
else:
    print("Положительных элементов в матрице нет.")
