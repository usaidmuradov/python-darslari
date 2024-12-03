def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
# print(summa(1, 2, 3, 4, 5))

def suma(*sonlar):
    return sum(sonlar)

# print(summa(1, 2, 3, 4, 6))

def summa(x, y, *sonlar):
    return x + y + sum(sonlar)

# print(summa(1))

def avto_info(kompaniya, model, **malumotlar):
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info('GM', 'Malibu', rang = 'Qora', narx = 25000, korobka = 'Avtomat')
# print(avto1)


####################################

def kupaytir(*sonlar):
    s = 1
    for i in sonlar:
        s *= i
    return s
kupaytma = kupaytir(1, 2, 3, 4)
# print(kupaytma)

# talaba_info ={}
def malumot_yarat(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

talaba_info = malumot_yarat('Umar', 'Saidmuradov', yosh = 19, universitet = 'NamDU', fakultet = 'Matematika', kurs = 2)
print(talaba_info)
