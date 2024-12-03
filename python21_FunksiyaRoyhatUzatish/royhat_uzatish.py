# talaba1 = input('1-talabanign ismini kiriting: ')
# talaba2 = input('2-talabanign ismini kiriting: ')
# talaba3 = input('3-talabanign ismini kiriting: ')
# talaba4 = input('4-talabanign ismini kiriting: ')
# talabalar = [talaba1,talaba2,talaba3,talaba4]
# print(talabalar)
# talabaBaholari ={}
# def talabaniBahola():
#     while talabalar:
#         talaba = talabalar.pop()
#         baho = input(f'{talaba.title()}ning baxosini kiriting: ')
#         talabaBaholari[talaba] = baho
#     return talabaBaholari
# baholandi = talabaniBahola()
# print(baholandi)
##################################

def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in  range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar
matnlar = ['hAsan', 'husan', 'umar', 'farrux', 'davron']
print(matnlar)
print(katta_harf(matnlar))

def baxola(talabalar):
    baxolar = {}
    for talaba in talabalar:
        baxo = input(f'{talaba.title()}ning baxosini kiriting: ')
        baxolar[talaba] = baxo
    return baxolar
baxolar = baxola(matnlar[:])
print(baxolar)