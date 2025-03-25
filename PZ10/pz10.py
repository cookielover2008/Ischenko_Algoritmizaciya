tours = {
    "Вояж": {"Мексика", "Канада", "Израиль", "Италия", "США"},  # Определяем туристические агентства и их туры
    "РейнаТур": {"Англия", "Япония", "Канада", "ЮАР"},
    "Радуга": {"США", "Испания", "Швеция", "Австралия"}
}
est_japan = {agency for agency, countries in tours.items() if "Япония" in countries}        #  В каких турагенствах можно приобрести туры в Японию
net_yuar = {agency for agency in tours if "ЮАР" not in tours[agency]}       #  В каких турагенствах нельзя приобрести туры в ЮАР
vse_tours = set()
for countries in tours.values():
    vse_tours.update(countries)

print("Турагентства, где можно приобрести туры в Японию:", est_japan)
print("Турагентства, где нельзя приобрести туры в ЮАР:", net_yuar)
print("Полный список всех туров:", vse_tours)