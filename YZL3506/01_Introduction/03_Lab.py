# Try - Except - Finally
# Uygulamalarda anlık olarak alınan hatalara (exception) yani istisnai durumlar diyoruz. Bu durumları try except blokları ile handle etmeye çalışyıoruz.
# try:
#     x = int(input('Tam sayı giriniz: '))
#     sonuc = x / 0
#     print(sonuc)
# except ZeroDivisionError as err:
#     print('Bir tam sayı sıfıra bölünemez.')
# finally:
#     print('Ne olursa olsun ben çalışırım')

try:
    # age = int(input('Age: '))
    # print(age)
    x = int(input('Tam sayı giriniz: '))
    sonuc = x / 0
    print(sonuc)
except ValueError as err:
    print(f'{err}')