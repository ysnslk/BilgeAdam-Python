# If else
# region Example 1
# Kullanıcıdan 2 adet sayı alalım ve bu sayılardan büyük olanı ekrana yazalım
# x = int(input("Enter the number first: "))
# y = int(input("Enter the number second: "))
# if x > y:
#     print('{x} is greater than {y}'.format(x=x, y=y))
# elif x < y:
#     print('{x} is less than {y}'.format(x=x, y=y))
# else:
#     print('{x} is equal to {y}'.format(x=x, y=y))
# endregion

# region Example 2
# Kullanıcıdan alına sayı çift mi tek mi?
# x = int(input("Enter a number: "))
# if x % 2 == 0:
#     print('{x} Çifttir'.format(x=x))
# else:
#     print('{x} tektir'.format(x=x))
# endregion

# region Example 3
# Kullanıcıdan alınan sayı pozitif mi negatif mi nötr mü?
# sayi = int(input("Sayı giriniz: "))
# if sayi > 0:
#     print(f'{sayi} pozitiftir')
# elif sayi == 0:
#     print(f'{sayi} nötrdür')
# else:
#     print(f'{sayi} negatiftir')
# # endregion

# region Example 4
# Kullanıcıdan mevsim bilgisi alalım. Gelen mevsime göre ayları ekrana yazalım.
# Bu soruyu match-case kullanarak yapalım. python 3.10 ile gelen yapıdır. if-else alternatifidir. Sadece string kontrollerde kullanabiliyoruz.
# parameter = input("Mevsimi Giriniz: ")
# match parameter:
#     case 'Sonbahar':
#         print('Eylül\nEkim\nKasım')
#     case 'Kış':
#         print('Aralık\nOcak\nŞubat')
#     case 'İlkbahar':
#         print('Mart\nNisan\nMayıs')
#     case 'Yaz':
#         print('Haziran\nTemmuz\nAğustos')
#     case _:
#         print('Lütfen geçerli bir mevsim giriniz.')
# endregion

# region Example 5
# Kullanıcıdan alınan araç türü ve hız bilgisi üzerinden cezalısın yada değilsin yazın
# car_type = input("Araç tipini giriniz: ")
# speed = int(input("Hızınızı giriniz: "))
# if speed < 0:
#     print("Lütfen negatif bir değer girmeyin.")
# else:
#     match car_type:
#         case 'Otomobil':
#             if (speed > 50):
#                 print('Cezalısın')
#             else:
#                 print('Cezalı değilsin')
#         case 'Kamyon':
#             if (speed > 30):
#                 print('Cezalısın')
#             else:
#                 print('Cezalı değilsin')
#         case 'Motorsiklet':
#             if (speed > 60):
#                 print('Cezalısın')
#             else:
#                 print('Cezalı değilsin')
#         case _:
#             print('Lütfen geçerli bir araç tipi giriniz.')
# endregion

# region Example 6
# Kullanıcıdan alınan 3 tane sayıdan büyük olanı ekrana yaz
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# n3 = int(input("Enter the third number: "))
# if n1 > n2 and n1 > n3:
#     print("The first")
# elif n2 > n1 and n2 > n3:
#     print("The second")
# else:
#     print("The third")
# endregion

# region Example 7
# Kullanıcıdan aradığı ürün bilgisini alıyoruz. Hangi reyonda ise ona yönlendiriyoruz.
# product = input("Enter the product you are looking for: ")
# if product in ['Salatalık', 'Domates', 'Patlıcan', 'biber']:
#     print('The product is in the produce section.')
# elif product in ['Bilgisayar', 'Telefon', 'Tablet']:
#     print('The product is in the technology section.')
# elif product in ['Masa', 'Sandalye', 'Koltuk']:
#     print('The product is in the furniture section.')
# else:
#     print('The product you requested is not in stock.')
# endregion

# region Example 8
# Kullanıcıdan satın aldığı kitap sayısını alalım
# Bir kitap 5Tl
# 1-20'dan arasında kitap alırsa %5
# 21-50'dan arasında kitap alırsa %10
# 511-75'dan arasında kitap alırsa %15
# 76-100'dan arasında kitap alırsa %20
# book = int(input("Satın aldığınız kitap sayısı: "))
# book_price = 5
# total = 0
# if 0 <= book <= 20:
#     total = (book_price * book) * 0.95
# elif 21 <= book <= 50:
#     total = (book_price * book) * 0.90
# elif 51 <= book <= 75:
#     total = (book_price * book) * 0.85
# elif 76 <= book <= 100:
#     total = (book_price * book) * 0.80
# else:
#     total = 0
#     print("Lütfen geçerli bir kitap sayısı giriniz")
# print(f'Ödenecek Tutar: {total}')
#endregion

# region Example 9
# Lineer bir doğrunun katsayılarını bulun
# delta = b ** 2 - 4 * a * c
# delta sıfırdan büyükse 2 kök
# delta sıfırsa 1 kök
# delta sıfırdan küçükse real kök yok
# from math import sqrt
# x_kare_katsayi = int(input("Karenin katsaysını giriniz: "))
# x_katsayi = int(input("katsayıyı giriniz: "))
# sabit_katsayi = int(input("sabit sayısını giriniz: "))
# delta = x_katsayi ** 2 - 4 * (x_kare_katsayi * sabit_katsayi)
# if delta > 0:
#     x1 = (-x_katsayi - sqrt(delta)) / (2 * x_kare_katsayi)
#     x2 = (-x_katsayi + sqrt(delta)) / (2 * x_kare_katsayi)
#     print(f'x1 = {x1}, x2 = {x2}')
# elif delta == 0:
#     x = (-x_katsayi) / (2 * x_kare_katsayi)
#     print(f'x = {x}')
# else:
#     print('Reel kök yoktur')
# endregion

# region Example 10
# Kullanıcıdan username, password, kilo, boy bilgilerini alalım
# Kullanıcı login olacak (beast, 123)
# bmi bilgisini vereceğiz.
# username = input("Username: ")
# password = input("Password: ")
# if username == 'beast' and password == '123':
#     print("Giriş Başarılı")
#     height = int(input("Boy giriniz(cm): "))
#     weight = int(input("Kilonuzu giriniz(kg): "))
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#         print(f"BMI = {bmi}. Zayıfsınız")
#     elif 18.5 <= bmi <= 24.9:
#         print(f"BMI = {bmi}. Normal")
#     elif 25 <= bmi <= 29.9:
#         print(f"BMI = {bmi}. Kilolu")
#     elif 30 <= bmi <= 34.9:
#         print(f"BMI = {bmi}. 1. derece obezite")
#     elif 35 <= bmi <= 39.9:
#         print(f"BMI = {bmi}. 2. derece obezite")
#     elif 40 <= bmi:
#         print(f"BMI = {bmi}. 3. derece obezite")
#     else:
#         print("Bmi hatalı. Lütfen geçerli bir boy ve kilo değerleri giriniz.")
# else:
#     print("Kullanıcı veya şifre hatalı")
# endregion