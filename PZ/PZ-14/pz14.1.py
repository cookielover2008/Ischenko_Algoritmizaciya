# В исходном текстовом файле(Dostoevsky.txt) найти все фамилии с инициалами
# (например, А. Ф. Куманиной и т.п.).

import re

with open('D:\PzManakova\pz14\Dostoevsky.txt', 'r', encoding='utf-8') as file:      # Открываем файл для чтения в кодировке utf-8
    text = file.read()

pattern = r'\b(?:[А-Я]\.\s){1,2}[А-Я][а-яё]+\b'     # Регулярное выражение для поиска инициалов + фамилии

matches = re.findall(pattern, text) # Ищем все совпадения

unique_matches = set(matches)       # Выводим фамилии с инициалами
for match in unique_matches:
    print(match)
