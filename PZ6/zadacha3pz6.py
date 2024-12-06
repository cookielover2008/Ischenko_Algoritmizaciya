def poshli_napravo(spisok):
    # Если список пустой, возвращаем пустой список
    if len(spisok) < 2:
        return []
    # Создаем новый список, ставим 0 в начало и добавляем все элементы, кроме последнего
    return [0] + spisok[:-1]

# Пример использования:
A = [1, 2, 3, 4, 5]
result = poshli_napravo(A)
print("Сдвинули! ", result)
