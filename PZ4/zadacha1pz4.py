#  Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2.

numb = int(input('Введите число больше нуля: '))  # пользователь вводит число
totalsum = 0
if numb > 0:                              # случай, когда n > 0
    sum1 = numb ** 2
    sum2 = (2 * numb) ** 2
    for i in range(1, numb + 1):
        summa = (numb + i) ** 2
        totalsum += summa
    print(totalsum + sum1 + sum2)
else:                                    
    print('Число должно быть больше 0')
