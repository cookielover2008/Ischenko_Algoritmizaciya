voyage = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reina_tour = {"Англия", "Япония", "Канада", "ЮАР"}
raduga = {"США", "Испания", "Швеция", "Австралия"}

# 1
japan = []
if "Япония" in voyage:
    japan.append("Вояж")
if "Япония" in reina_tour:
    japan.append("РейнаТур")
if "Япония" in raduga:
    japan.append("Радуга")

# 2
no_south_africa = []
if "ЮАР" not in voyage:
    no_south_africa.append("Вояж")
if "ЮАР" not in reina_tour:
    no_south_africa.append("РейнаТур")
if "ЮАР" not in raduga:
    no_south_africa.append("Радуга")

# 3
all_tours = voyage | reina_tour | raduga

print("1. Япония:", japan)
print("2. Не ЮАР:", no_south_africa)
print("3. Все туры:", all_tours)
