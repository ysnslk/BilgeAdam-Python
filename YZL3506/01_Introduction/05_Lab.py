
# For Loop
# For Loop'a geçmeden önce incelememiz gereken yardımcı fonksiyon ve operatör bulunmaktadır.
# Bunlar "in" , "not in" ayrıca range() built-in fonksiyonlardır.

# "in" & "not in"
# name = 'mike tyson'
# # not: string ifadeler karakter listeleridir.
#
# print('b' in name)  # output => false
# print('m' in name)  # output => true
# print('M' in name)  # output => false
#
# # not in operatoru
# print('M' not in name)  # output => true
# print('m' not in name)  # output => false

# Not: fonksiyonalrın içerisine verdiğimiz argümanlara göre fonksiyonlar farklı işler icra ederler.
# Burada farklı işlerden kastımız birbirinden alakasız işlemler değildir.
# Ana bir iş mantığının farklı versiyonalrıdır. Aşağıdaki range fonksiyonunu bu cümleye göre inceleyelim.

# range() => range fonksiyonun ana iş mantığı bize bir sayı listesi dönmesidir. range aldığı argumanlara gore yaratacağı sayı listesinin özellikleri farklılaşmaktadır
# 1 argüman aldığında => default olarak 0'dan başlayarak argüman olarak verilen tamsayı(n-1) olarak bir tamsayı listesi döner.

# for i in range(10):
#     print(i, end=",")
#
# 2 argüman aldığında range(10,20) bu durumda 10 dan başlayıp 19 a kadar gıder
# for i in range(10,20):
#     print(i, end=",")
# 3 argüman aldığında => range(10,101,5) bu durumda 10dan başlayıp 100 e kadar 5 er 5 er artacak sekılde bır lıste olusturur
# for i in range(10,101,5):
#     print(i, end=",")

# 0 -100 arasında ki çift ve tek sayıların toplamlarını ayrı ayrı ekrana yazdıralım
# toplamcift = 0
# toplamtek = 0
# for i in range(0,100):
#     if i%2==0:
#         toplamcift = toplamcift + i
#     else:
#         toplamtek = toplamtek + i
# print(f'Toplamcift = {toplamcift} , toplamtek = {toplamtek}')

# başlangıç, bitiş ve artış miktarlarını kullanıcının belirlediği bir range() fonksiyobundaki ger bir sayının karesını hesaplayarak ekrana yazdıralım
# baslangic = int(input('Baslangic sayisi giriniz: '))
# bitis = int(input('Bitiş sayisi giriniz: '))
# aralik = int(input('Aralik sayisi giriniz: '))
#
# for i in range(baslangic, bitis, aralik):
#     print(f'{i} sayisinin karesi {i*i}\n')

# Faktöriyel hesaplama yapalım

# sayi=int(input("Faktöriyelini almak istediğiniz sayıyı giriniz: "))
# faktoriyel = 1
# if sayi < 0:
#     print("Sayı 0 dan küçük olamaz")
# else:
#     for i in range(1,sayi+1):
#         faktoriyel *= i
#     print(faktoriyel)

# Nested for Loop
# for i in range(10):
#     for j in range(10):
#         pass
#
# Çarpım tablosu istiyoruz
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i*j}')

# X sembollerini kullanarak içi dolu dikdörtgen yapın
# kenar1= int(input('1. Kenarı giriniz: '))
# kenar2= int(input('2. Kenarı giriniz: '))
# for i in range(kenar1):
#     for j in range(kenar2):
#         print('X', end=' ')
#     print()


# x sembolü ile dik üçgem yapalım
# for i in range(5):
#     for j in range(i+1):
#         print('X', end=' ')
#     print()