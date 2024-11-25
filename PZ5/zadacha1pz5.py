def shagi_to_zero(n):
    steps = 0
    while n > 0:        
        summa_cifr = 0                   # Вычисляем сумму цифр
        for cifra in str(n):            # Проходим по каждой цифре числа
            summa_cifr += int(cifra)    # Превращаем цифру в число и добавляем к сумме
        n -= summa_cifr                 # Вычитаем сумму цифр из числа
        steps += 1                      # Увеличиваем счетчик шагов
    return steps
N = input("Введите число N: ")          # Ввод N
while type(N) != int:                   # обработка исключений для N
        try:
            N = int(N)
        except ValueError:
            print("Неправильно ввели!")
            N = input("Введи N заново: ")
result = shagi_to_zero(N) 
print("Количество шагов, необходимых для достижения нуля:", result)  # Выводим результат
