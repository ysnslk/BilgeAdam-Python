# While Loop
# Tekrarlı işlemleri yaptırmak istediğimiz zaman yercih ettiğimiz bir  mekanizmadır.
# While loop bir saayac ile birlikte bir karar mekanizmasına sahip bir yapıdır.Sayac artırılıp azaldılarak her defasında şarta bakılıp şart tuttuğu sürece
# döngünün dönmesi temin edilir.

# sayac = 0
# while sayac < 100:
#   business logic
#   sayac += 1

# region Example 1
# 0 ile 100 arasındali sayıları ekrana yazdıralım
# sayac = 0
# while sayac <= 10:
#     print(sayac)
#     sayac += 1

# endregion

# region Example 2
# 1 ile 100 arasındaki sayıları toplayarak nihai sonucu ekrana yazdıralım.
# sayac = 1
# toplam = 0
# while sayac <= 100:
#     toplam = toplam + sayac
#     sayac += 1
#
# print(toplam)
# endregion

# region Example 3
# 1 ile 100 arasındaki sayıların çift ve tek toplamlarını ayrı ayrı ekrana yazdıralım toplayarak nihai sonucu ekrana yazdıralım.
# sayac = 1
# toplamtek = 0
# toplamcift = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         toplamcift= toplamcift + sayac
#
#     else:
#         toplamtek = toplamtek + sayac
#     sayac += 1
#
# print(f'Tek sayıların toplamı = {toplamtek} , Çift sayıların toplamı = {toplamcift}')
# endregion

# region Example 4
# 1 ile 100 arasındaki sayıların kaç tanesı çift ve kaç tanesı tek  ayrı ayrı ekrana yazdıralım
# sayac = 0
# teksayac = 0
# ciftsayac = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         ciftsayac += 1
#
#     else:
#         teksayac += 1
#     sayac += 1
#
# print(f'Tek sayıların adedi = {teksayac} , Çift sayıların adedi = {ciftsayac}')
# endregion

# region Example 5
# Kullanıcıdan işlem türü alıyoruz (e, +, -, *, /) alalım.alınan işlem türüne göre ilgili işlemi yapalım ve çıktısını ekrana yazdıralım.
# Kullanıcı 'e' işlemini gönderene kadar sınırsız sayıda 4 işlem yapabilsin
# print("Hesaplama sistemine hoşgeldiniz.")
# a= True
# while a:
#     islem = input("İşlem türünü giriniz. Çıkış için e ye basınız: ")
#     if islem == "e":
#         a = False
#     elif islem == "+" or islem == "-" or islem == "*" or islem == "/":
#         sayi1 = float(input("Birinci sayıyı giriniz: "))
#         sayi2 = float(input("İkinci sayıyı giriniz: "))
#         sonuc = eval(f"{sayi1} {islem} {sayi2}")
#         print("Sonuç:", sonuc)
#     else:
#         print("Yanlış bir işlem girdiniz.")


# endregion

# region Example 6
# Kullanıcıdan alınan sayı asal mı değil mi?

# sayi = int(input("Bir sayı giriniz: "))
# sayac = 2
# asal = True
# if sayi < 2:
#     print("2 den büyük değerlerde sorgulama yapabilirsiniz")
# elif sayi >= 2:
#     while sayac<sayi:
#         if sayi % sayac == 0:
#             asal = False
#             break
#         else:
#             sayac += 1
#     if asal == False:
#         print(f'{sayi} sayısı asal bir sayı değildir.')
#     else:
#         print(f'{sayi} sayısı asal bir sayıdır.')
# else:
#     print('Geçersiz bir sayı girişi yaptınız')



# endregion

# region Example 7
# Kullanıcıdan alınan sayının Faktöriyeli hesaplayalım
# sayifakt=int(input("Lütfen bir sayı giriniz: "))
# sayac = 1
# sonuc = 1
# if sayifakt < 0:
#     print('Sayı sıfırdan küçük olamaz')
# else:
#     while sayac <= sayifakt:
#         sonuc = sayac * sonuc
#         sayac += 1
#     print(f'{sayifakt} sayısının faktöriyeli = {sonuc}')


# endregion

