# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:07:13 2024

@author: User
"""

mevalar = ['olma', 'anjir', 'anor']
print(mevalar)
narxlar = [1200, 8, 387]
bozorlik = ['gosht', 'sabzi', 'kartoshka', 'piyoz']
mahsulot1 = bozorlik.pop(3)
print('men '+ mahsulot1 + ' sotib oldim')
print('sotib olinmagan mahsulotlar ', bozorlik)
#amaliyot
dostlar = ['Abror', 'Farrux', 'Ibroxim', 'Davron', 'Ayyub']
print('salom dostim ', dostlar[1])
print('salom ', dostlar[0], ', bugun dasturimizni yakunlaymizmi')
t_shahslar = ['Imom Buxoriy', 'Al-Xorazmiy', 'Ibn Sino', 'Islom Karimov']
z_shahslar = ['Davronbek Turdiyev', 'Messi', 'Xabib', 'Macan']
print('men tarixiy shahslardan ',t_shahslar.pop(0),'bilan, zamonaviy shahslardan esa ', z_shahslar.pop(0),' bilan birga ishlashni xohlardim')
t_shahslar.append('Karimiov Musoxon')
print(t_shahslar)
z_shahslar.remove('Messi')
# %%
print(z_shahslar)

