import random

# List
# Uygulama içerisinde anlık olarak bizim bir yada birden fazla değer tutan yapılardır. Farklı tiplerde değerler
# tutabilirler. Listelerde RAM üzernde .... alanında tutulduğu için değişkenler gibi uygulama sonlandığında ilk
# RAM' den uçurular yani Runtımate(Uygulama çalışırken) içerisine eklenilen değerleri Hard Disk gibi saklayamazlar.

# Listeler index mantığı ile çalışır. Liste içerisinde saklanılan değerler sıfırıncı index'ten başlayarak pozitif yönde
# artan index değerlerinde depolanırlar. Yani 1. index'te tutulan değerler ulaşmak için index değerlerin yani 1 kullanabilirim

# top_boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfiled', 'Rocky Marciano']
# print(top_boxers[0])

# region Task 1
# George Forman bilgisini top_boxers listesinin sonuna ekleyelim
# top_boxers.append('George Foreman')
# print(top_boxers)

# endregion

# region Task 2
# Antony Joshua bilgisini top_boxers listesinin sonuna ekleyelim
# top_boxers.insert(4,'Antony Joshua')
# print(top_boxers)
# endregion

# region Task 3
# Antony Joshua bilgisini top_boxers listesinden silelim
# top_boxers.remove('Antony Joshua')
# print(top_boxers)
# endregion

# region Task 4
# 5. indexteki bilgiyi top_boxers listesinden silelim
# top_boxers.pop(5)
# print(top_boxers)
# endregion

# region Task 4
# aşağıdaki current_boxers listesi ile top_boxers listesini birleştirelşim
# current_boxers = ['Antony Joshua', 'Tyson Fury', 'Deantony Wilder']
# top_boxers.extend(current_boxers)
# print(top_boxers)

# endregion

# region Task 5
# sayilar isimli bir liste içerisine otomatik oalrak random 10 tane sayı ile dolduralım
# sayilar = []
# for i in range(10):
#     random_sayi=random.randint(1,500)
#     sayilar.append(random_sayi)
# print(sayilar)
# endregion

# region Task 6
# Kullanıcıdan bir söz öbeği alalım. Örneğin "Merhaba ben burak yılmaz"
# Bütün harfleri küçük harfe dönüştürün
# ilgili söz öbeğindeki sesli harfleri, sesli_harfler listesine ekleyelim
# Sessiz harfleri sessiz listesine ekleyeceğiz.
# her harf bir defa kullanılabilir.
# rakam varsa rakamlar elenmeli
# metin = input("Metin giriniz. ")
# turkish_vowels = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
# sesli_harfler = []
# sessiz_harfler = []
# for i in metin:
#     if i.isdigit() or i == " ":
#         pass
#     elif i.lower() in turkish_vowels:
#         if i.lower() in sesli_harfler:
#             pass
#         else:
#             sesli_harfler.append(i.lower())
#     else:
#         if i.lower() in sessiz_harfler:
#             pass
#         else:
#             sessiz_harfler.append(i.lower())
# print(f'Sesli harfler: {sesli_harfler}\n'
#    f'sessiz harfler: {sessiz_harfler}')


# is.alpha() built in fonksiyonu ile ilgili karakter a-z yada A-Z harf aralıgında mı diye bakar
# endregion

# region Task 7
# İki listeyi random sayılar ile dolduralım
# akabinde benzer index'lerde tutulan değerleri toplayarak 3. listede yine aynı indexte yazdıralım
# sayilist1 = [random.randint(1, 100) for _ in range(10)]
# sayilist2 = [random.randint(1, 100) for _ in range(10)]
# newlist = []
#
# for i in range(10):
#     newlist.insert(i, sayilist1[i]+sayilist2[i])
# print(f'sayilist1: {sayilist1}\nsayilist2: {sayilist2} \nnewlist: {newlist}')
# endregion

# region Task 8
# users listesi içerisinde bulunan kullanıcılara kurumsal mail adresleri oluşturalım
# örneğin burak.yilmaz@bilgeadam.com
# users = ['burak yilmaz', ' ertuğrul', 'bora eden erdem', 'kerim andul cabbar okkes', ' ']
# mail_address = []
# for user in users:
#     user_names = user.split(' ')
#     for item in user_names:
#         if item == '':
#             user_names.remove(item)
#     if user == " ":
#         pass
#     elif len(user_names) >= 2:
#         mail_address.append(f"{user_names[0]}.{user_names[-1]}@bilgeadam.com")
#
# print(mail_address)
# endregion

# region Task 9
# Kullanıcının girdiği passwordler valid mi
# en az bir büyük bir küçük harf olmalı
# en az bir rakam olmalı
# en az bir tane noktalama işareti olmalı
# herhangi bir ifade tekrar etmemeli
# endregion

# List Comprehansion
# [expression for item in liste if condition]
# rakamları list comprehansion kullanarak ekrana yazdırın
print([item for item in range(10)])

power = [item * item for item in range(10)]
print(power)

print([i * i for i in range(100) if i % 3 == 0])