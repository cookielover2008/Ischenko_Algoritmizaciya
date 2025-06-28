# Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
# шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
# "кличка" и "порода".


class Animal:
    def __init__(self, vid, paws, color):
        self.vid = vid
        self.paws = paws
        self.color = color

class Sobaka(Animal):
    def __init__(self, vid, paws, color, klichka, poroda):
        super().__init__(vid, paws, color)
        self.klichka = klichka
        self.poroda = poroda

    def display_info(self):
        print(f"Вид: {self.vid}")
        print(f"Количество лап: {self.paws}")
        print(f"Цвет шерсти: {self.color}")
        print(f"Кличка: {self.klichka}")
        print(f"Порода: {self.poroda}")

dog = Sobaka("Собака", 4, "рыжий", "Шарик", "Овчарка")
dog.display_info()
