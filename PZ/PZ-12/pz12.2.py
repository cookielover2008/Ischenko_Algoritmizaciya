# Из заданной строки отобразить только цифры. Использовать библиотеку string.
# Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
# 481 feet (147 metres) high.

import string

def extract_digits(s): yield from [char for char in s if char in string.digits]
print("".join(extract_digits(input("Введите строку: "))))

