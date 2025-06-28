# . Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите
# метод, который выводит информацию о здании в формате "Адрес: адрес, Количество
# этажей: этажи".

class Building:
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

    def display_info(self):
        print(f"Адрес: {self.address}, Количество этажей: {self.floors}")

building1 = Building("ул. Ленина, 1", 5)
building1.display_info()

building2 = Building("ул. Пушкина, 10", 3)
building2.display_info()

building3 = Building("пр. Победы, 25", 10)
building3.display_info()
