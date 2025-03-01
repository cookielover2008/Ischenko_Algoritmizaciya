#   Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
#   Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
#   Австралия. .Определить:
#   1. в каких турагенствах можно приобрести туры в Японию.
#   2. в каких турагенствах нельзя приобрести туры в ЮАР.
#   3. полный список всех туров.

voyage = {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'}
reynatour = {'Англия', 'Япония', 'Канада', 'ЮАР'}
rainbow = {'США', 'Испания', 'Швеция', 'Австралия'}

est_japan = []
net_yuar = []
def est_li (a, b, c):
    if 'Япония' in voyage or reynatour or rainbow:
        est_japan.append(voyage or reynatour or rainbow)
    if 'ЮАР' not in voyage or reynatour or rainbow:
        net_yuar.append(voyage or reynatour or rainbow)
    return est_japan
    return net_yuar


est_li(voyage, reynatour, rainbow)


print('Турагенства с туром в Японию: ', est_japan)
print('Турагенства без туров в ЮАР: ', net_yuar)
print('Все туры: ', voyage|reynatour|rainbow)
