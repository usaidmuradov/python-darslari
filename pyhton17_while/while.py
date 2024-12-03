# while
# ism = input('ismingi nima? ')
# t_yil = int(input(f'Salom {ism.title()}, Nechanchi yilda tugilgansiz? '))
# yosh = 2024 - t_yil
# print(f'siz {yosh} yosh ekansiz')
# son = int(input('1 dan 9 gacha bolgan sonni tanlang: '))
# while son<=10:
#     print(son, end=' ')
#     son += 1
# print('dastur tugadi')
# print('kiritilgan sonni kvadratini hisoblovchi dastur')
# savol = 'istalgan sonni kiriting, agar dasturni yakunlamoqchi bolsangiz "exit" deb yozing: '
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(int(qiymat)**2)
#     else:
#         print('dastur yakunlandi!')
# ishora = True
# while ishora ==True:
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(int(qiymat)**2)
#     else:
#         ishora = False
#         print('dastur yakunlandi!')
# while True: #toxtamaydigan tsik
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(int(qiymat)**2)
# print('dastur yakunlandi!')
# sonlar = list(range(1, 101))
# for son in sonlar:
#     if son == 12:
#         break
#     print(f'{son} ning kvadrati {son**2} ga teng')
# sonlar = list(range(1, 10))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f'{son} ning kvadrati {son**2} ga teng')
################################################################################################
#amaliyot
# while True:
#     kitob = input('Yaxshi ko\'rgan kitobingiz nomini kiriting (dasturni yakunlash uchun "exit" ni kiriting): ')
#     if kitob == 'exit':
#         break
#     else:
#         print(f'Sizning yaxshi ko\'rgan kitobingiz: {kitob}')
# print('Dastur tugadi')
# while yosh:
#     yosh = input('yoshingizni kiriting: ')
#     if (yosh=='exit' or yosh=='quit'):
#         break
#     elif (int(yosh)<7):
#         print('siz uchun chipta narxi 2000')
#     elif (int(yosh)<18 and int(yosh)>=7):
#         print('siz uchun chipta narxi 3000')
#     elif (int(yosh)<65 and int(yosh)>=18):
#         print('siz uchun chipta narxi 10000')
#     else:
#         print('siz uchun kirish bepul')
# print('dastur tugadi')

# fishka = True
# while fishka == True:
#     yosh = input('yoshingizni kiriting: ')
#     if (yosh=='exit' or yosh=='quit'):
#         fishka = False
#     elif (int(yosh)<7):
#         print('siz uchun chipta narxi 2000')
#     elif (int(yosh)<18 and int(yosh)>=7):
#         print('siz uchun chipta narxi 3000')
#     elif (int(yosh)<65 and int(yosh)>=18):
#         print('siz uchun chipta narxi 10000')
#     else:
#         print('siz uchun kirish bepul')
# print('dastur tugadi')


# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol = "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# fishka = True
# while fishka == True:
#     qiymat = input(savol)
#     if type(qiymat) == 'string':
#         if qiymat == 'exit':
#             fishka = False
#             print('dastur yakunlandi')
#         elif qiymat != 'exit':
#             print("Bu yerda xatolik!")
#             continue
#     else:
#         if int(qiymat)>=0:
#             ildiz = float(qiymat)**(0.5)
#             print(f"{qiymat} ning ildizi {ildiz} ga teng")
#         elif int(qiymat)<0:
#             print("Musbat son kiriting!")
#             continue
# exit deb yozsa dastur tugasin, musbat son kiritsa ildizini topsin, manfiy son kiritsa musbat son kiritishini sora  qolgan hollar uchun xatolik roy berdi deb habar chiqarsin va dastur qaytalansin
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if str(qiymat)=='exit':
        print('dastur yakunlandi')
        break
    elif int(qiymat)>0:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    elif qiymat!='exit':
        print('Musbat son kiriting')
        continue
        
