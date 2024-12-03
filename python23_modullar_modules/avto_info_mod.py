def avto_info(kompaniya, model, rang, korobka, yil):
    avto={
        'kompaniya':kompaniya,
        'model':model,
        'rang':rang,
        'korobka':korobka,
        'yil':yil,
        # 'narxi':narxi
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
        # narxi=input('narxi: ')
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili))
        javob = input('yana avtomobil qoshishni istaysizmi (ha/yoq): ')
        if javob=='yoq':
            break
    return avtolar
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil")