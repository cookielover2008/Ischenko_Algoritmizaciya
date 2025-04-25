# .В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди отрицательных
# 2. элементы кратные двум
# 3. их сумму

import random
seq = [random.randint(-100, 100) for i in range(10)]

neg_max = max(filter(lambda x: x < 0, seq))
even = list(filter(lambda x: x % 2 == 0, seq))
even_sum = sum(even)

print("Максимальный среди отрицательных:", neg_max)
print("Элементы, кратные двум:", even)
print("Сумма элементов, кратных двум:", even_sum)
