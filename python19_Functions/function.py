#function
# def salom_ber():

#     print('Assalomu alekum')
# salom_ber()

# def salom_ber(ism):
#     """"Foydalanuvchidan ismini qabul qilib, unga salom beruvchi funtion"""
#     print(f'Assalomu alekum, hurmatli {ism.title()}')
# salom_ber('muhammad')
# print(salom_ber.__doc__)

########################################

#amaliyot
# ism = input('Ismingizni kiriting: ')
# yosh = int(input('Yoshingni kiriting: '))
# def function(ism, yosh):
#     print(f'Hurmatli {ism.title()}, siz {2024-yosh}-yil ekansiz')

# function(ism, yosh)
# son = int(input('Sonni kiriting: '))
# def function(a):
#     print(f'{a} sonining kvadrati: {son**2}')
#     print(f'{a} sonining kubi: {son**3}')
# function(son)
# son = int(input('Sonni kiriting: '))
# def function(son):
#     if son%2 == 0:
#         print(f'{son} soni juft son')
#     else:
#         print(f'{son} soni toq son')
# function(son)
son = int(input('Sonni kiriting: '))
sonlar = list(range(2, 11))
def function(son):
    for n in sonlar:
        if son%n == 0:
            print(f'{son} soni {n} ga qoldiqsiz bo\'linadi')
        else:
            print(f'{son} soni {n} ga qoldiqsiz bo\'lmaydi')
function(son)