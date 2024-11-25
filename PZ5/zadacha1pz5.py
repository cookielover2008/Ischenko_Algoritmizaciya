def summa_cyfr(n):
    return sum(int(digit) for digit in str(n))
def shagi_do_zero(n):
    shagi = 0
    while n > 0:
        n -= summa_cyfr(n)
        shagi += 1
    return shagi

n = input('Введите число N: ')
while type(a) != int:                   # обработка исключений для N
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите A заново: ")
rezultat = shagi_do_zero(n)           
print('Количество шагов до нуля: ', rezultat)
