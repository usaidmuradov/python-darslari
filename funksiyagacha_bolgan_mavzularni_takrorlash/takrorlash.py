# #1. Oʻzgaruvchilar va maʼlumot turlari

# #1-masala
# ism = input('ismingizni kiriting: ')
# familiya = input('familiyangizni kiriting: ')
# yosh = int(input('yoshingizni kiriting: '))
# tugilgan_yil = 2024 - yosh
# print(f'\nSizning ismingiz {ism}, familiyangiz {familiya}, va siz {tugilgan_yil}-yilda tugilgansiz')
# #2-malasa
# a = int(input('a soninizni kiriting: '))
# print(a)
# b = int(input('siz ishlayotgan dasturlash tilini kiriting: '))
# print(f'{b} dasturi')

# #2. Matn bilan ishlash

# # 1-masala
# # 2-masala

# #3. Roʻyxatlar va ularning metodlari
# # 1-masala
# mevalar = ["olma", "banan", "uzum"]
# mevalar.append('anjir')
# mevalar.remove('uzum')
# print(mevalar)
# # 2-masala
# sonlar = []
# while True:
#     son = int(input('sonni kiriting: '))
#     sonlar.append(son)
#     takrorlash = input('yana son qoshishni istaysizmi(ha/yoq)? ')
#     if takrorlash == 'yoq':
#         break
#     else:
#         continue
# print(f'kiritilgan sonlarning eng kichigi: {min(sonlar)}')
# print(f'kiritilgan sonlarning eng kattasi: {max(sonlar)}')

# #4. Shart operatorlari

# # 1-masala
# son = int(input('sonni kiriting: '))
# if son > 0:
#     print(f'{son} soni musbat')
# elif son < 0:
#     print(f'{son} soni manfiy')
# else:
#     print(f'{son} soni, manfiy ham emas, musbat ham emas')
# # 2-masala
# yosh = int(input('Yoshingizni kiriting: '))
# if yosh > 18:
#     print('Siz voyaga yetgansiz')
# else:
#     print('Siz voyaga yetmagansiz')

# # 5. Takrorlanish operatorlari

# # 1-masala
# min = int(input('oraliq boshini kiriting: '))
# max = int(input('oraliq oxirini kiriting: '))
# for i in range(min, max+1):
#     print(i)
# # 2-masala
# while True:
#     son = int(input('sonni kiriting: '))
#     print(son**2)
#     takrorlash = input('yana son qoshishni istaysizmi(ha/yoq)? ')
#     if takrorlash == 'yoq':
#         break

# # sinov savollari
# #1-savol: Python-da list va tuple oʻrtasidagi farqlarni tushuntiring.
# #javob: list ustida biz xohlagancha amallar bajarishimiz mumkin, unga elemnt qoshish, element olib tashla va hokozo, tuple esa ozgarmasdir, agar uni ozgartirmoqchi bolsak ham oldin uning type ni list ga ozgartirishimiz kerak
# #2-savol: Quyidagi kod nima chiqadi?
# #javob: Katta

# matn = " Python Python python pytHon"
# print(matn.count("Python"))  # 2

# Topshiriq 1: Matndan so‘zlar sonini hisoblash
# soz = input('gap kiriting: ')
# print(len(soz.split()))

# # Topshiriq 2: Belgilarni hisoblash
# soz = input('sozni kiriting: ')
# if soz.isalpha() == True:
#     print(len(soz))
# else:
#     print('Bu soz harflardan iborat emas')

# # Topshiriq 3: Matnni teskari o‘girish
# matn = input('matn kiriting: ')
# print(matn[::-1])

# # Topshiriq 4: Gapni so‘zlarga ajratish va qayta birlashtirish
# matn = input('matn kiriting: ')
# matn1 = matn.split()
# matn2 = " ".join(matn1)
# print(matn2.title())

# # Topshiriq 5: Belgi sanash
# matn = input('matn kiriting: ')
# takror = input('takror sozni kiriting: ')
# print(f'"{takror}" sozi matnda {matn.count(takror)} marta qatnashgan')

talabalar = []

def talaba_qosh():
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    yosh = int(input("Yoshi: "))
    fakultet = input("Fakulteti: ")
    bosqich = int(input("Bosqichi: "))
    baholar = {}
    while True:
        fan = input("Fan nomini kiriting (yoki 'stop' yozib tugating): ")
        if fan.lower() == 'stop':
            break
        baho = int(input(f"{fan} fanidan baho: "))
        baholar[fan] = baho
    talaba = {
        "ism": ism,
        "familiya": familiya,
        "yosh": yosh,
        "fakultet": fakultet,
        "bosqich": bosqich,
        "baholar": baholar
    }
    talabalar.append(talaba)

def talaba_korish():
    for talaba in talabalar:
        print(f"\nTalaba: {talaba['ism']} {talaba['familiya']}")
        print(f"Yoshi: {talaba['yosh']}, Fakulteti: {talaba['fakultet']}, Bosqichi: {talaba['bosqich']}")
        print("Baholar:")
        for fan, baho in talaba['baholar'].items():
            print(f"  {fan}: {baho}")

def baholar_tahlili():
    for talaba in talabalar:
        print(f"\n{talaba['ism']} {talaba['familiya']}ning qayta topshirishi kerak bo‘lgan fanlari:")
        qayta_topshirish = [fan for fan, baho in talaba['baholar'].items() if baho < 3]
        if qayta_topshirish:
            print(", ".join(qayta_topshirish))
        else:
            print("Hamma baholari yaxshi!")

def boshqaruv():
    while True:
        print("\n[1] Talaba qo‘shish")
        print("[2] Talabalarni ko‘rish")
        print("[3] Baholarni tahlil qilish")
        print("[4] Chiqish")
        tanlov = input("Tanlovni kiriting: ")
        if tanlov == '1':
            talaba_qosh()
        elif tanlov == '2':
            talaba_korish()
        elif tanlov == '3':
            baholar_tahlili()
        elif tanlov == '4':
            break
        else:
            print("Noto‘g‘ri tanlov, qayta urinib ko‘ring!")

boshqaruv()

# talabalar = []
# ism = input('ismingizni kiriting: ')
# familiya  = input('familiyangizni kiriting: ')
# yosh = input('yoshingizni kiriting: ')
# fakultet = input('Fakultetingizni kiriting: ')
# fan = input('baholnishi kerak bolgan fan nomini kiriting: ')
# baxo = input(f'{fan}dan baxosini kiriting: ')
