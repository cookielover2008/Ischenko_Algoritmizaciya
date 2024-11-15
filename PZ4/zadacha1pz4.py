#  Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2.

numb = input('Введите N (N > 0): ')# пользователь вводит число
while type(numb) != int:                   # обработка исключений для n
    try:
        numb = int(numb)
    except ValueError:
        print("Неправильно ввели!")
        numb = input("Введи N заново: ")
totalsum = 0
if numb > 0:                                     # случай, когда n > 0
    sum1 = numb ** 2                             # вычисляем первое число
    sum2 = (2 * numb) ** 2                       # вычисляем последнее число
    for i in range(1, numb + 1):                 # цикл для промежуточных вычислений
        summa = (numb + i) ** 2
        totalsum += summa
    print(totalsum + sum1 + sum2)
else:                                            # случай, когда n <= 0
    print('Число должно быть больше 0')
