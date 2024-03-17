# Değer Döndüren Fonksiyonlar (Returnable)
lst =[12,11,19,2,99]
lst_1 = []
lst_2 = []

# lst içerisinde ki çift sayıları 2 ile çarparak lst_1 içerisine ekleyelim. tek sayıları 3 ile çarparakk lst_2'ye ekleyelim.
# def tek_cift_mi(sayi: int):
#     if sayi %2 == 0:
#         return 'cift'
#     else:
#         return 'tek'
#
#
# def append_list(result: str, sayi: int) -> None:
#         if result == 'cift':
#             lst_1.append(sayi * 2)
#         else:
#             lst_2.append(sayi * 3)
#
#
# def main():
#     for i in lst:
#         result = tek_cift_mi(i)
#         append_list(result, i)
#     print(lst_1)
#     print(lst_2)
#
#
# main()


# Kullanıcıdan alında 3 tane sayıyı topladıktan sonra karesini alarak sonucu ekrana yazdıralım

# def toplam(s1: int,s2: int,s3: int) -> int:
#     return s1+s2+s3
#
# def karesini_hesapla(sayi: int) -> None:
#     print(f'Sonuç: {sayi ** 2}')
#
# def main():
#     x = int(input('Sayi: '))
#     y = int(input('Sayi: '))
#     z = int(input('Sayi: '))
#
#     sonuc = toplam(x,y,z)
#
#     karesini_hesapla(sonuc)
#
# # karesini_hesapla(toplam(x,y,z)) yıukarıdaki iki satırı bu şekilde yazabiliriz
#
# main()

# Aşağıdali listede bulunan rakamların liste içerisinde geçme sıklıklarını bulun ve sözlük tipinde çıktı verin.rakamın kendisi key geçme sıklığı value olacak şekilde
# rakamlar = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 4, 2, 2, 4, 3, 5]
#
# def frequency_count(numbers: list) -> None:
#     frequency_dict = {}
#
#     for item in numbers:
#         if item in frequency_dict:
#             frequency_dict[item] += 1
#         else:
#             frequency_dict[item] = 1
#
#     for key, value in frequency_dict.items():
#         print(f'Key: {key} - Value: {value}')
#
#
# frequency_count(rakamlar)

# Bir söz öbeğinde tekrar eden kelimelerden arındırarak çıktı verelim
# örnek input=> merhaba ben burak burak ben burak
# çıktı merhaba ben burak

# def repeat_words(sentence: str) -> None:
#     lst = []
#     result = ''
#
#     for item in sentence.split(' '):
#         if item not in lst:
#             lst.append(item)
#     result = ' '.join(lst)
#     print(result)
#
#
# input = "ahmet mehmet her zaman mehmet ahmet keser"
# cikti = repeat_words(input)

# Kullanıcıdan alına söz öbeğinde ki kelimeleri alfabetik olarak sıralayalım.
# def sort_word(sentence: str) -> None:
#     words = []
#     for item in sentence.split(' '):
#         words.append(item)
#
#     words.sort()
#     print(words)
#
# sort_word(input("Enter a sentence: "))

# Kullanıcı sign in sign up
user_dict = {
    '1': {
        'user_name': 'beast',
        'password': '123'
    },
    '2': {
        'user_name': 'savage',
        'password': '123'
    }
}

def sign_up():
    print("Kaydolma")
    new_user_name = input("Yeni kullanıcı adı: ")
    if any(kullanici['user_name'] == new_user_name for kullanici in user_dict.values()):
        print("Bu kullanıcı adı zaten mevcut. Lütfen farklı bir kullanıcı adı seçin.")
        return
    new_password = input("Yeni parola: ")
    user_id = str(len(user_dict) + 1)
    user_dict[user_id] = {'user_name': new_user_name, 'password': new_password}
    print("Kayıt başarıyla tamamlandı.")

def sign_in():
    print("Giriş yapma")
    user_name = input("Kullanıcı adı: ")
    password = input("Parola: ")
    for user_id, user_info in user_dict.items():
        if user_info['user_name'] == user_name and user_info['password'] == password:
            print("Giriş başarıyla yapıldı.")
            return
    print("Hatalı kullanıcı adı veya parola. Lütfen tekrar deneyin.")

def main():
    while True:
        print("\n1. Kaydol\n2. Giriş yap\n3. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            sign_up()
        elif secim == "2":
            sign_in()
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")


main()


