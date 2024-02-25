# Değişken nedir ?
# Algoritma konusunda çalışırken kutulara benzetmiştik. Kullanıcıdan alınan değeri depoladığımız şeylerdir.Sabit için değer tutan yapılardır.

# Diğer programlama dillerinde bir değişken tanımlarken ilk önce ilgili değişkenin tutacağı değere göre bir tip geçilir.
# Örneğin:
# int x = 5; (değişkenin tip bağımlılığı)

# Python'da değişken tanımlama
# Pyhton'da değişken tanımlarken diğer proglama dilleriğinde olduğu gibi tip belirtmiyoruz. Python'da değişkenler su gibidir. Nasılsa su girdiği kabın şeklini alırsa python'da değişkene atılan değerin tipini alır.
# x = 5
# print(x)  # Python'da built-in fonksiyonudur. Yani python'ın çekirdek dosyasnına gömülmüş bir fonksiyondur.
# Fonksiyon => Üzerine bir görev atanmış hazır yapılardır. İstediğimiz yerde istediğimiz kadar çağırıp kullanabiliriz.
# print(type(x))  # burada da type() built-in bir fonksiyondur. İçerisine verdiğimiz değerin tipini ekrana yazar.
# x = 'Mike Tyson'
# print(x)
# print(type(x))
# x = True
# print(x)
# print(type(x))

# Kullanıcıdan 2 adet sayı alaım ve temel 4  işlem yapalım.
# x = int(input("Lütfen bir sayı giriniz: "))
# y = int(input("Lütfen bir sayı giriniz: "))
# toplam = x + y
# cikarma = x - y
# carpma = x * y
# bolme = x / y
# print(f'Toplam: {toplam}')
# print(f'Çıkarma: {cikarma}')
# print(f'Çarpma: {carpma}')
# print(f'Bölme: {bolme}')

# print(f'Sonuc:', toplam)
# print('Sonuc: {}'.format(toplam))
# print('{} + {} = {}'.format(x, y, toplam))

# Kullanıcıdan alınan kenar bilgisine göre karenein alanını ve çevre bilgisini hesaplayınız.
# x = int(input("Karenin bir kenarını giriniz: "))
# alan = x * x
# cevre = 4 * x
# print(f'Alan : {alan}')
# print(f'Çevre : {cevre}')

# Dikdörtgenin alanını ve çevresini hesaplayın

x = int(input("Dikdörtgenin kısa kenarını giriniz: "))
y = int(input("Dikdörtgenin uzun kenarını giriniz: "))
print('Alan: {}'.format(x * y))
print('Çevre: {}'.format(2 * (x + y)))
