import math
import random
from functools import reduce
uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi, 20))

kvadrat = lambda x, y : x**y
# print(kvadrat(3, 3))

def daraja(n):
    return lambda x : x**n

# print(daraja(2)(7))

sonlar = list(range(1,11))
ildizlar = list(map(math.sqrt, sonlar))
# print(ildizlar)

kvadratlar = list(map(lambda x: x**x, sonlar))
# print(kvadratlar)

a = [1,2,3,4,5,6,7,8]
b = [9,10,11,12,13,14,15,16,17]
a_plus_b = list(map(lambda x,y: x+y, a ,b))
# print(a_plus_b)

sonlar = random.sample(range(1, 101), 5)
# print(sonlar)
def juftmi(x):
    return x % 2 == 0
# print(juftmi(3))
juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)
juft_sonlar = list(filter(lambda x: x % 2==0, sonlar))
# print(juft_sonlar)

mevalar = ['olma', 'anor', 'anjir', 'behi', 'shaftoli', 'xurmo', 'o\'rik', 'banan']
# harf = 'b'
b_bilan_boshlanadigan = list(filter(lambda meva:meva.startswith('u'),mevalar))
# print(b_bilan_boshlanadigan)
qisqaMeva = list(filter(lambda meva: len(meva)<=5, mevalar))
# print(qisqaMeva)


########################
#amaliyot
#1-masala
sonlarim = list(range(1, 11))
kvadrati = list(map(lambda son: math.pow(son, 2), sonlarim))
# print(kvadrati)

#2-masala
mevalar = ['olma', 'anjir', 'uzum']
uzunligi = list(map(lambda uzunlik: len(uzunlik), mevalar))
# print(uzunligi)

#3-masala
sonlar = [8, 3, 7, 1, 5]
juft_sonlar = list(filter(lambda juft: juft%2==0, sonlar))
# print(juft_sonlar)

#6-malasa
son = [19]
juft_yoki_toq = list(map(lambda juft: 'juft' if juft%2==0 else 'toq', son))
# print(juft_yoki_toq)

#7-masala
sonlar = random.sample(range(1, 101), 10)
# print(sonlar)
kattasi = reduce(lambda a, b: a if a>b else b, sonlar)
kichigi = reduce(lambda a, b: a if a<b else b, sonlar)
# print(f'eng kattasi: {kattasi}')
# print(f'eng kichigi: {kichigi}')

#8-masala
mevalar = ['olma', 'anor', 'anjir', 'behi', 'shaftoli', 'xurmo', 'o\'rik', 'banan']
saralash = sorted(mevalar, key=lambda soz:len(soz), reverse=True)
# print(saralash) 

#9-masala
a = [1,2,3,4,5,6,7,8]
b = [9,10,11,12,13,14,15,16,17]
a_plus_b = list(map(lambda x,y: x+y, a ,b))
# print(a_plus_b)

#10-masala
sonlar = random.sample(range(-100, 101), 10)
musbat_sonlar = list(filter(lambda son: son>0, sonlar))
print(sonlar)
print(musbat_sonlar)