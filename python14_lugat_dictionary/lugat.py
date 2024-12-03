# Dictionary(lug'at)
# car_0 = {'model': 'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
# en_uz = {'apple':'olma', 'apricot':'orik', 'banana':'banan'}
talaba ={'ism': 'umar', 'yosh': '19', 't_yil': '2005'}
talaba['kurs'] = 2
talaba['fakultet'] = 'matematika'
# print(talaba)
del talaba['t_yil']
# print(talaba)
familiyasi = talaba.get('familiyas', 'uning familiya malumoti yoq')
# print(familiyasi)
# amaliyot
# otam = {'ism': 'Husanxon', 'yosh': '48'}
# onam = {'ism': 'Mohlaroy', 'yosh': '44'}
# ukam = {'ism': 'Saidmurod', 'yosh': '12'}
# opam = {'ism': 'Zakovat', 'yosh': '21'}
# print(f'Otamning ismi {otam['ism']}, {otam['yosh']} yoshdalar')
# print(f'Onamning ismi {onam['ism']}, {onam['yosh']} yoshdalar')
# print(f'Opamning ismi {opam['ism']}, {opam['yosh']} yoshda')
# print(f'Ukamning ismi {ukam['ism']}, {ukam['yosh']} yoshda')
# ranglar = {'kulrang': 'grey', 'yashil': 'green', 'qizil': 'red', 'sariq': 'yellow', 'qora': 'black','ko\'k': 'blue'}
# kiritilgan_rang = input('rangni tanlang: ')
# rang = ranglar.get(kiritilgan_rang, 'Lugatizmizda bunday rang mavjud emas')
# print(rang)
# ranglar = {'kulrang': 'grey', 'yashil': 'green', 'qizil': 'red', 'sariq': 'yellow', 'qora': 'black','ko\'k': 'blue'}
# kiritilgan_rang = input('rangni tanlang: ')
# if kiritilgan_rang in ranglar:
#     print(ranglar[kiritilgan_rang])
# else:
#     print('Lugatizmizda bunday rang mavjud emas')