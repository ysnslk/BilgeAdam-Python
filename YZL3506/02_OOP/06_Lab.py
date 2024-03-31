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
# from math import pow, factorial
# from time import sleep,time
#
# def calculate_time_execute(func):
#     def inner_func(*args, **kwargs):
#         start_time = time()
#         sleep(10)
#         result = func(*args, **kwargs)
#         end_time = time()
#         print(f"{func.__name__} fonksiyonu {end_time - start_time} saniyede çalıştırıldı")
#         return result
#     return inner_func
#
# @calculate_time_execute
# def us_alma(a: int, b: int):
#     print(f'Sonuç: {pow(a, b)}')
#
# @calculate_time_execute
# def faktoriyel_hesaplama(number: int):
#     print(f'Sonuç: {factorial(number)}')
#
# @calculate_time_execute
# def toplama(x: int, y: int, z: int):
#     print(f'Sonuç: {x + y + z}')
#
# us_alma(2, 3)
# faktoriyel_hesaplama(5)
# toplama(3, 4, 5)

# endregion

# region metaclass
# Python'da metaclass, başka sınıfları yaratmak için kullanılan bir sınıftır. Bir sınıf kendi instance'ının nasıl davranacağını tanımlar. Lakin metaclass bir sınıfın nasıl davranacağını tanımlar . Genellikle sınıf oluşturma davranışını özelleştirme ve sınıfın otomatik olarak hangi özel fonskiyonlara sahip olacağını belirlemek için kullanıyoruz.
# endregion

# region Abstract Example 1
from abc import ABC, abstractmethod

class BaseMuzikAleti:
    def __init__(self,brand,model):
        self.model = model
        self.brand = brand

class Gitar(BaseMuzikAleti):
    def __init__(self,brand,model,tel):
        super().__init__(brand,model)
        self.tel = tel

class Keman(BaseMuzikAleti):
    def __init__(self,brand,model,kasa):
        super().__init__(brand,model)
        self.kasa = kasa


class Muzisyen:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.caldigi_ensturmanlar = []

# BaseService sınıfımız ABC meta sınıfından kalıtım alarak artık syout sınıf özellğine kavuşmuştur.
class BaseService(ABC):

    # Abstract bir sınıf içersinde herhangi bir methodu "@abstractmethod" decoratorü ile işaretlersek bu method soyut bir method artık soyut bir method olmuştur.
    # Abstract olarak işaretlenmiş bir fonksiyonun gövdesi olmaz yani ilgili fonksiyona bir business logic yüklenmez. Bu bağlamda aşağıdaki methodu "pass" diyerek oona gövde atamadık.
    # Neden abstract metodlara gövde yazılmaz?
    # Çünkü abstract olarak işaretlenmiş methodlar alt sınıflarda override edilmesi zorunludur. Bunun nedeni kontrat durumudur.

    @abstractmethod
    def call_sound(self) -> str: pass

    def hello_everyone(self):
        print('Hi')

    @abstractmethod
    def harmonize(self) -> str: pass

class GitarService(BaseService):
    def call_sound(self) -> str:
        return 'Gitar sesi'
    def harmonize(self) -> str:
        return 'Akort Edildi'

    def salve(self):
        print('Salvat')

class KemanService(BaseService):
    def call_sound(self) -> str:
        pass

    def harmonize(self) -> str:
        pass

    # Bu methodu ister override ederiz istersek etmeyiz çünkü ata sınıfta soyut olarak işaretli değil.
    def hello_everyone(self):
        print('Kimseyi selamlamak istemiyorum..!')

def main():
    gitar_service = GitarService()
    keman_service = KemanService()

    gitar = Gitar('Fender','Classical Gitar','Kaliteli tel')
    keman = Keman('Godrigez','Classical','Meşe')

    muzisyen = Muzisyen('Yasin','Solak')
    muzisyen.caldigi_ensturmanlar.append(gitar)
    muzisyen.caldigi_ensturmanlar.append(keman)

    print(f'Ad: {muzisyen.first_name}\n'
          f'Soyad: {muzisyen.last_name}\n'
          f'Çaldığı Enstürman: {muzisyen.caldigi_ensturmanlar[0].brand}\n'
          f'Çaldığı Enstürman: {muzisyen.caldigi_ensturmanlar[0].model}\n'
          f'Çıkardığı Ses: {gitar_service.call_sound()}\n'
          f'Akor Edildi: {gitar_service.harmonize()}')
main()
# endregion