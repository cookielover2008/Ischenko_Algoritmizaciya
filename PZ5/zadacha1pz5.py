def summa_cifr(n):
    return sum(int(digit) for digit in str(n))
def shagi_do_zero(n):
    shagi = 0
    while n > 0:
        n -= summa_cifr(n)
        shagi += 1
    return shagi

n = input('Введите число N: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Неправильно веели!')
rezultat = shagi_do_zero(n)
print('Количество шагов до нуля: ', rezultat)