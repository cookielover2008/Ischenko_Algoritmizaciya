# Определить количество дней в введенном месяце для невисокосного года
month = input('Введи число от 1 до 12: ')
while type(month) != int:                   # обработка исключений для month
    try:
        month = int(month)
    except ValueError:
        print("Неправильно ввели!")
        month = input("Введите месяц заново: ")
try:
    if month in (1, 3, 5, 7, 8, 10, 12):
        print('В этом месяце 31 день')
    elif month in (4, 6, 9, 11):
        print('В этом месяце 30 дней')
    elif month == 2:
        print('В этом месяце 28 дней')
    else:
        print('Введи правильное число месяца.')
except ValueError:
    print('Ошибка ввода')
    
