# Дан список A размера N и целое число K (1 < K < N).
# Вывести элементы список с порядковыми номерами, кратными K: AK, A2*K, A3*K,... .
# Условный оператор не использовать.
A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]  # Создаем список A
N = len(A)                                                      # Заданный размер списка
K = input('Введи число(> 1): ')                                      # Задаём значение K
while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        print('Неправильно ввели!')
        K = input("Введи K заново: ")


result = []                              # Создаём пустой список для хранения результата


for i in range(K, N, K):            # Используем цикл для перебора индексов от K до N с шагом K
    result.append(A[i])


print(result)                       # Выводим результат