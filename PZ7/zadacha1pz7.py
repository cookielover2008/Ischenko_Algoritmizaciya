# Запрос строки от пользователя
originalnaya_strochka = input("Введите строку: ")

# Разворот строки с явным циклом
perevernutaya_strochka = ''
for bukva in originalnaya_strochka:
    perevernutaya_strochka = bukva + perevernutaya_strochka

# Вывод результирующей строки
print("Строка в обратном порядке:", perevernutaya_strochka)