# Nesting
# car0 = {
#     'model': 'lacetti',
#     'rang': 'oq',
#     'yil': 2018,
#     'narx': 13000,
#     'km': 50000,
#     'korobka': 'avtomat'
# }
# car1 = {
#     'model': 'nexia 3',
#     'rang': 'qora',
#     'yil': 2015,
#     'narx': 9000,
#     'km': 89000,
#     'korobka': 'mexanika'
# }
# car2 = {
#     'model': 'gentra',
#     'rang': 'qizil',
#     'yil': 2019,
#     'narx': 15000,
#     'km': 20000,
#     'korobka': 'mexanika'
# }
# cars =[car0, car1, car2]
# for car in cars:
#     print(f"Model: {car['model']}, Rang: {car['rang']}, Yil: {car['yil']}, Narx: {car['narx']} so'm, Km: {car['km']} yurgan, Korobka: {car['korobka']}")
# print(cars)
# print(cars[0])
# print(cars[0]['km'])
# malibus = []
# for n in range(10):
#     newCar = {
#         'model': 'malibu',
#         'rang': None,
#         'yil': 2024,
#         'narx': None,
#         'km': 0,
#         'korobka': 'avto'
#     }
#     malibus.append(newCar)
# for malibu in malibus[0:3]:
#     malibu['rang'] = 'qizil'

# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
    
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka'] = 'mexanika'
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narxi'] = 40000
#     else:
#         malibu['narx'] = 35000
# print(malibus)

# dasturchilar = {
#     'muhammad': ['python', 'javascript'],
#     'umar': ['c++', 'html'],
#     'abdulloh': ['php', 'js'],
#     'ayyub': ['c#', 'sql'],
#     'ibroxim': ['python', 'react'],
# }

# for ism, tillar in dasturchilar.items():
#     print(f'\n{ism.title()} quyidagi dasturlash tillarini biladi')
#     for til in tillar:
#         print(til.upper())

#############################################3

#amaliyot


# anvar = {
#     'ism': 'Anvar',
#     'familiya': 'Nazrullayev',
#     'soha': 'IT',
#     'yoshi': 41
# }
# musoxon = {
#     'ism': 'Muso',
#     'familiya': 'Karimov',
#     'soha': 'Matematika',
#     'yoshi':  75
# }
# andrey = {
#     'ism': 'Andrey',
#     'familiya': 'Kriliyev',
#     'soha': 'Artist',
#     'yoshi': 22
# }
# davron = {
#     'ism': 'Davron',
#     'familiya': 'Turdiyev',
#     'soha': 'Mnomonika',
#     'yoshi': None
# }

# mashxurlar = [anvar, musoxon, andrey, davron]

# for mashxur in mashxurlar:
#     if mashxur['yoshi'] == None:
#         print(f'{mashxur['ism']} {mashxur['familiya']}, mutaxassisligi: {mashxur['soha']}')
#     else:
#         print(f'{mashxur['ism']} {mashxur['familiya']}, mutaxassisligi: {mashxur['soha']}, yoshi: {mashxur['yoshi']}')
# davron.setdefault('kitoblar', [])
# davron['kitoblar'].append('Defolt sistemasi')
# davron['kitoblar'].append('Xotira')
# davron['kitoblar'].append('Monemonist')
# print(davron)

ismi = input('ismingni yoz: ')
kinolar = []
for malumot in range(3):
    kinolar.append(input(f'{malumot+1}-kino nomini yoz: '))
favoriteFilm = {
    ismi: [kinolar[0], kinolar[1], kinolar[2]]
}
print(favoriteFilm)




