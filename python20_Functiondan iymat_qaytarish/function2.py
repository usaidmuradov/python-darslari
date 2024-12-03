#Function dan qiymat qaytarish
# def avto_info(kompaniya, model, rang, korobka, yil, narxi=None):
#     avto={
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rang,
#         'korobka':korobka,
#         'yil':yil,
#         'narxi':narxi
#     }
#     return avto
# avto1 = avto_info('GM', 'Malibu', 'qora', 'Avromat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'oq', 'mexanika', 2018, 15000)
# print('Online bozordagi mavjud avtomobilllar:')
# # print(avto1)
# # print(avto2['narxi'])
# avtolar =[avto1, avto2]
# # print(avtolar[0]['model'])
# for avto in avtolar:
#     print(f'{avto["model"]} - {avto["kompaniya"]}, {avto["rang"]} rangi, {avto["korobka"]} korobka, {avto["yil"]} yil, {avto["narxi"] if avto["narxi"] else "bepul"} narx')
# def oraliq(min, max, qadam):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# # print(oraliq(1, 11))
# print(oraliq(1, 11, 2))
# print(oraliq(1, 11))


def avto_info(kompaniya, model, rang, korobka, yil, narxi=None):
    avto={
        'kompaniya':kompaniya,
        'model':model,
        'rang':rang,
        'korobka':korobka,
        'yil':yil,
        'narxi':narxi
    }
    return avto


def avto_kirit():
    avtolar=[]
    while True:
        print('Quyidagi malumotlarni kiriting:')
        kompaniya=input('ishlab chiqaruvchi: ')
        model=input('Model: ')
        rangi=input('Rangi: ')
        korobka=input('Korobka: ')
        yili=input('Ishlab chiqarilgan yil: ')
        narxi=input('narxi: ')
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        javob = input('yana avtomobil qoshishni istaysizmi (ha/yoq): ')
        if javob=='yoq':
            break
    return avtolar
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")











##########################################
#amaliyot
# def foydalanuvchi_info(ism, familiya, t_yil, t_joy, tel_raqam=None):
#     avto={
#         'ism':ism,
#         'familiya':familiya,
#         't_yil':t_yil,
#         'yosh': 2024-t_yil,
#         't_joy':t_joy,
#         'tel_raqam':tel_raqam
#     }
#     return avto
# malumotlari= []
# while True:
#     print('Quyidagi malumotlarni kiriting:')
#     ism=input('Ismingiz: ')
#     familiya=input('Familiyangiz: ')
#     t_yil=int(input('Tugilgan yilingi: '))
#     t_joy=input('Tugilgan joyingi: ')
#     tel_raqam=input('Telefon raqamingiz(ixtiyoriy): ')
#     malumotlari.append(foydalanuvchi_info(ism,familiya,t_yil,t_joy,tel_raqam))
#     javob = input('yana malumotlar kiritishni istaysizmi(ha/yoq): ')
#     if javob == 'yoq':
#         break
# print('foydalanuvchi malumotlari:')
# for foydalanuvchi in malumotlari: 
    
    # print(f'{foydalanuvchi["ism"].capitalize()} {foydalanuvchi["familiya"].capitalize()}, {foydalanuvchi["t_yil"]} - {foydalanuvchi["t_joy"]}, {foydalanuvchi["yosh"]} yoshda, {foydalanuvchi["tel_raqam"] if foydalanuvchi["tel_raqam"] else "Nomalum"}')
# son1 = int(input('birinchi sonni kiriting: '))
# son2 = int(input('ikkinchi sonni kiriting: '))
# son3 = int(input('uchinchi sonni kiriting: '))
# def eng_kattasini_chiqar(son1, son2, son3):
#     if son1>son2:
#         if son1>son3:
#             return son1
#         else:
#             return son3
#     else:
#         if son2>son3:
#             return son2
#         else:
#             return son3
#     return son1, son2, son3
# engKattasi = eng_kattasini_chiqar(son1, son2, son3)
# print(engKattasi)
# radius = int(input('Aylananing radiusini kiriting: '))
# def aynalananing_radiusini_top(radius, pi=3.14):
#     aylana = {
#         'diametr' : radius*2,
#         'uzunligi' : 2*radius*pi,
#         'yuzi' : radius**2*pi
#     }
#     return aylana
# radiuss = aynalananing_radiusini_top(radius)
# print(radiuss)

# def oraliq(min, max, qadam):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# # print(oraliq(1, 11))
# print(oraliq(1, 11, 2))
# # print(oraliq(1, 11))


# start = int(input('oraliq boshini kiriting: '))
# end = int(input('oraliq oxirini kiriting: '))


# def oraliq(start, end):
#     tubSonlar = []
#     for son in range(start, end+1):
#         if son < 2:
#             continue
#         elif son == 2:
#             tubSonlar.append(son)
#         else: 
#             for i in range(2, int(son**(1/2))+1):
#                 if son % i == 0:
#                     break
#             else: 
#                     tubSonlar.append(son)
#     return tubSonlar

# print(oraliq(start, end))

# start = int(input('oraliq boshini kiriting: '))
# end = int(input('oraliq oxirini kiriting: '))

# tubSonlar = []
# def oraliq(start, end):
#     for son in range(start, end + 1):
#         if son == 1:  # 1 ni o'tkazib yuboramiz
#             continue
#         elif son == 2:  # 2 ni bevosita qo'shamiz
#             tubSonlar.append(son)
#         else:
#             for i in range(2, int(son**(1/2)) + 1):  # ildizgacha bo'lgan sonlarni tekshiramiz
#                 if son % i == 0:
#                     break
#             else:  # agar hech bo'linmasa, tub son
#                 tubSonlar.append(son)
#     return tubSonlar

# print(oraliq(start, end))


