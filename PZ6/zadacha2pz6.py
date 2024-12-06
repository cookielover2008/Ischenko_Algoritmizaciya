#Дан список размера N. Найти количество его промежутков монотонности
#(то есть участков, на которых его элементы возрастают или убывают).
def schitaem_ciferki(spisok):
    if len(spisok) < 2:
        print('Невозможно выполнить операцию! Введи список снова')
        return []
    

    schet = 0           # Cчётчик промежутков монотонности    
    povishenie = None       # Задаем начальное состояние
    
    for i in range(1, len(spisok)):
        if spisok[i] > spisok[i - 1]:  # Если текущий элемент больше предыдущего
            if povishenie is False:  # Если до этого был убывающий участок
                schet += 1
            povishenie = True  # Устанавливаем состояние как возрастающее
        elif spisok[i] < spisok[i - 1]:  # Если текущий элемент меньше предыдущего
            if povishenie is True:  # Если до этого был возрастающий участок
                schet += 1
            povishenie = False  # Устанавливаем состояние как убывающее   
    if povishenie is not None:      # Если последний участок был монотонным, то добавляем его
        schet += 1

    return schet

# Пример использования
spisok = [3, 1, 2, 4, 3, 5, 6, 2]  # Примерный список
print('Ваш список: ', spisok)
result = schitaem_ciferki(spisok)
print("Количество промежутков монотонности:", result)
