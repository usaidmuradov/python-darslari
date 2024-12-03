# talaba = {
#     'ism': 'umar',
#     'familiya': 'saidmuradov',
#     'yosh': 19,
#     'universitet': 'NamDU',
#     'fakultet': 'Matematika',
#     'kurs': 4
# }
# # for kalit, malumoti in talaba.items():
# #     print(f'Kalit: {kalit}')
# #     print(f'Malumoti: {malumoti}')
# # print(talaba.keys())
# for malumot in talaba.keys():
#     print(malumot.title())
# amaliyot
# ranglar = {'kulrang': 'grey', 'yashil': 'green', 'qizil': 'red', 'sariq': 'yellow', 'qora': 'black','ko\'k': 'blue'}
# for u,e in sorted(ranglar.items()): 
#     print(f'{u} rangi ingliz tilida {e} bo\'ladi')
# poytaxt = {
#     'O\'zbekiston': 'Toshkent',
#     'Saudia Arabistoni': 'Ar-Riyod',
#     'Rossiya': 'Moskva',
#     'Norvegiya': 'Stokgolm',
#     'Xitoy': 'Pekin',
#     'Singapur': 'Singapor',
# }
# # for d, p in sorted(poytaxt.items()):
# #     print(f'{d} - {p}')
# davlat = input('Davlat nomini kiritng: ')
# if davlat in poytaxt.keys():
#     print(f'{davlat} davlatining poytaxti - {poytaxt[davlat]}')
# else:
#     print("Bunday davlat ma'lumotlari lug'atda mavjud emas.")
taomlar = {
    'palov': 20000,
    'lag\'mon': 25000,
    'chuchvara': 20000,
    'shashlik': 15000,
    'qozonkabob': 30000,
    'sho\'rva': 150000,
    'grill': 25000,
    'moshkichiri': 15000,
    'garoh': 18000,
    'mastava': 16000,
}
ovqatlar = []
print('Quyida siz ichmoqchi bo\'lgan 3 taom nomi kiriiting')
for ovqat in range(3):
    ovqatlar.append(input(f'{ovqat+1} - taomni kiriting: '))
# print(ovqatlar)
for buyurtma in ovqatlar:
    if buyurtma in taomlar:
        print(f'{buyurtma} taomining narxi - {taomlar[buyurtma]} so\'m')
    else:
        print(f'Bunday taom mavjud emas')
