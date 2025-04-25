# Из исходного текстового файла (pazzl.html) выбратьвсе html-коды изображений.
# Посчитать их количество.

import re
text = open("Dostoevsky.txt", "r+", encoding="utf-8").read()

ex = re.compile(r'\b([А-ЯЁ][.])\s([А-ЯЁ][.])\s([А-ЯЁа-яё]+)\b')
print(ex.findall(text))