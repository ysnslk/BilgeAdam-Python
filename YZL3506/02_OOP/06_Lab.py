# Abstraction (Soyutlama)
# OOP yapıları arasında en öenmlisidir.
# Üst seviyeli yazılım prensiplerine ve tasarım desenlerine uymak istiyorsak kod bloklarımızda soyutlam muhakkak olmalıdır. Soyutlama ile amaçlanan ana mantık şudur: Ata sınıfları soyut yaparak alt sınıflara kural koymak. Bir başka değiş ile ata sınıf ile alt sınıf arasında kontrat yada sözleşme imzalıyoruz. Gerçek hayatta nasıl kontrat bozulmazsa yazılım da bozulmaz.


# Soyutlamaya geçmeden önce öğrenmemiz gereken 1-2 husus bulunmaktadır. Bunlardan 1. decorator bir değer ise meta class

# region Decorator
# python programlama dilinde kullanılan bir keyword'tür. Bir fonksiyonu bir decorator ile var olan yeteneği üzerine bir yetenek daha ekleyebiliriz. Methodlarımızı yoğun kod yazmadan yeni bir yetenek ile extend etmiş oluyoruz. Python'da built-in bir çok decorator vardır. Bunlardan bazıları @abstrcatmethod,@static,@property vb. tabiiki custom decorator yazılabilir.
# def uppercase_name(function):
#     def inner_func():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return inner_func
#
# def get_fullname():
#     return 'Mike Tyson'
#
# print(uppercase_name(get_fullname)())
#
# @uppercase_name
# def get_name():
#     return 'Yasin Solak'
#
# print(get_name())
from math import pow, factorial
from time import sleep, time

def calculate_time_execute():
    pass
@calculate_time_execute
def us_alma(a: int, b: int):
    print(f'Sonuç: {pow(a, b)}')


def faktoriyel_hesaplama(number: int):
    print(f'Sonuç: {factorial(number)}')


def toplama(x: int, y: int, z: int):
    print(f'Sonuç: {x + y + z}')


us_alma(2, 3)
faktoriyel_hesaplama(5)
toplama(3, 4, 5)
# endregion
