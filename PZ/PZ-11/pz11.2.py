# Из предложенного текстового файла (text18-10.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив после последней строки автора и название
# произведения.

f = open("text18-10.txt", "r", encoding="utf-8")
rl = f.readlines()
text = "".join(rl)
f.close()

fo = open("text18-10-output.txt", "w", encoding="utf-8")
[fo.writelines(i) for i in rl]
fo.writelines("\nМ.Ю. Лермонтов\nНазвание: Бородино")
fo.close()

cnt = 0
[cnt := cnt + 1 for s in text if s.isupper()]

print(text)
print("Количество заглавных букв:", cnt)
