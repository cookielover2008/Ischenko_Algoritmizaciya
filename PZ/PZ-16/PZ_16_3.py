# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять
# информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. Использовать модуль
# pickle для сериализации и десериализации объектов Python в бинарном формате.

import pickle
from PZ_16_1 import building1, building2, building3

def save_def(zdaniya, file):
    with open(file, 'wb') as f:
        pickle.dump(zdaniya, f)

def load_def(file):
    with open(file, 'rb') as f:
        return pickle.load(f)


save_def([building1, building2, building3], 'zdaniya.pkl')

load_zdaniya = load_def('zdaniya.pkl')

for dom in load_zdaniya:
    dom.display_info()
