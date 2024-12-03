# print('Yaqin dostlaringiz royhatini tuzmamiz')
# ismlar = []
# fishka = True
# n=1
# while fishka == True:
#     ism = input(f'{n}-dostingiz ismini kiriting: ')
#     ismlar.append(ism)
#     takrorlash = input('yana ism qoshishni istaysizmi(ha/yoq)')
#     n = n+1
#     if takrorlash != 'ha':
#         fishka = False
# print('dostlaringiz royhati: ')
# for ism in ismlar:
#     print(ism.title())
# dostlar = {}
# ishora = True
# while ishora == True:
#     ism = input('Do\'stingiz ismini kiriting: ')
#     yosh = input(f'{ism.title()}ning yoshini kiriting: ')
#     dostlar[ism] = int(yosh)
#     davomi = input('Yana davom ettirishni istaysizmi?(ha/yoq)')
#     if davomi == 'yoq':
#         ishora = False
# for ism,yosh in dostlar.items():
#     print(f'{ism.title()} - {yosh} yoshda')
# cars = ['BMW', 'Mercedes', 'Toyoto', 'Mercedes', 'Muda', 'Mercedes']
# while 'Mercedes' in cars:
#     cars.remove('Mercedes')
# print(cars)
# talabalar = ['abdurahmon', 'umar', 'diyotbek']
# baholangan_talabalar = {}
# while talabalar: #while talabalar--> talabalar elementi tugagunga qadar 
#     talaba = talabalar.pop()
#     if talaba == 'diyorbek':
#         print('unga tugridan tugri 5')
#     else:
#         baho = input(f'{talaba.title()}ning baxosini kiriting: ')
#         print(f'{talaba.title()} baholandi')
#         baholangan_talabalar[talaba] = int(baho)
    
# print(baholangan_talabalar)


################################################################################################
#amaliyot
print('Marketingiz uchun mahsulot va uning narxlari royhatini tuzamiz')
mahsulot_narx={}
while True:
    mahsulot = input('Mahsulot nomini kiriting: ')
    narx = input('Mahsulot narxini kiriting: ')
    mahsulot_narx[mahsulot] = int(narx)
    yana = input('Yana davom ettirishni istaysizmi(ha/yoq): ')
    if yana == 'yoq':
        break
print('Mahsulotlaringiz va uning narxi:')
for mahsulotlar,narxlar in mahsulot_narx.items():
    print(f'{mahsulotlar}ning narxi - {narxlar} so\'m')

# ++++++++++++++++++++++++++++++++++++++++++++++++
print('Bozorlik mahsulotlari royhatini tuzamiz')
# bozorlik  = []
fishka = True
while fishka == True:
    a = (input('Mahsulot nomini kiriting: '))
    if a in mahsulot_narx:
        print(f'{a}ning narxi - {mahsulot_narx[a]} so\'m')
    else:
        print('bizda bunday mahsulot yoq')
    takrorlash = input('yana mahsulot kiritishni istaysizmi?(ha/yoq): ')
    if takrorlash == 'yoq':
        print('dastur yakunlandi')
        fishka = False
# print('Harid qilish kerak bolgan mahsulotlar:')
# for mahsulotlar in bozorlik:
    # print(mahsulotlar)


