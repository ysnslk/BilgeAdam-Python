# Python programlama dilinde bir nesne yaratmak için class anahtar sözcüğünü kullanıyoruz. class ile tanımalddığımız yapı içerisnde yaratacağımız ya da projemizde ihtiyaç duyduğumuz (objenin) özelliklerini tanımlıyoruz. Class'ları gerçek dünyada ki prototiplere benzetebiliriz.

# class Vehicle:
#     # Attirbute (özellikleri) tanımladık.
#     door_number = 0
#     brand = ''
#     model = ''
#     engine_size = ''
#     torque = 0

# Aşağıda Vehicle() sınıfından bir nesne ürettik.Yazılım dünyasında buna çıkartma (instance) denir.
# x = Vehicle()
# x.brand = 'Mercedes'
# x.model = 'C'
# x.engine_size = 5
# x.torque = 4
# print(f'Brand: {x.brand}')

# Artık istediğimiz yerde istediğimiz kadar Vehicle() sınmıfıdan nesne üretebiliriz. Nasıl ki built-in nesnesini istediğimiz yerde istediğimiz kadar kullanabiliyorsak custom nesneler içinde geçerlidir.
#
# y = Vehicle()
# y.brand = 'Ford'
# y.model = 'Shellby'
# y.door_number = 4
# y.engine_size = 6
# y.torque = 5
# print(f'Brand: {y.brand} '
#       f'Model: {y.model} '
#       f'Door number: {y.door_number} '
#       f'EngineSize: {y.engine_size} '
#       f'Torque: {y.torque}')

# Yukarıda instance alırken ilgili class_name() şeklinde kullandık yani fonksiyon gibi kullandık. Burada sınıf içerisinde hazır olarak bulunan __init__() fonksiyonunu kullandık yani onu call ettik. __init__() fonksiyonu ilgili sınıfı başlatmaya (initilaze) etmeye yaramaktadır. Bir başka değiş ile sınıfımız kullanımza kazırlamaktır. Ram'in heap alanına çıkarmaktadır.

# class Boxer:
#     alias=''
#     def __init__(self,first_name,last_name):
#         # aşağıda ki "adi" ve "soyadi" attirbute'leri içn object attirbute denir.
#         self.adi = first_name
#         self.soyadi = last_name
#         # self sınıfı temsil eder.
#
#
#
# boxer_1 = Boxer(first_name='Mike', last_name='Tyson')
# print(dir(Boxer))
# print(dir(boxer_1))
# boxer_1.alias= 'Iron'
# print(boxer_1.__dict__)
# boxer_2 = Boxer(first_name='Mike', last_name='Tyson')
# print(dir(boxer_2))

# Circle isminde bir sınıf yaratalım
# pi adında bir class attirbute olsun
# r adında bir object attirbute olsun
# alan ve çevre hesaplama fonksiyonları olsun

# class Circle:
#     pi = 3.14
#
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return self.pi * self.r ** 2
#
#     def perimeter(self):
#         return 2 * self.pi * self.r
#
# yari_cap = float(input("Yarı Çapı: "))
# circle1 = Circle(yari_cap)
# print("Alanı:", circle1.area())
# print("Çevresi:", circle1.perimeter())

# Departmant adında bir sınıf oluşturalım
# departmant_name ve employee_count class attirbute
# name,age object attirbute
# show_information() olsun
# show_employee_count() fonksiyonu olsun. Departmant sınıfndan her instance aldığında employee_count 1 arttırılsın ve bu arttırma işleminin sonucu ekrana yazılsın.

# class Departman:
#     department_name = ''
#     employee_count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Departman.employee_count += 1
#         print("Employee count increased to", Departman.employee_count)
#
#     def show_information(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Departmant:",self.department_name)
#
#     def show_employee_count(self):
#         print("Total Employee count:", self.employee_count)
#
# employee1 = Departman("Ali", 30)
# employee2 = Departman("Veli", 25)
# employee3 = Departman("Yasin", 28)
#
# employee1.show_information()
# employee2.show_information()
# employee3.show_information()

# Software Developer  adında bir sınıf yaratalım.
# first_name, last_name object attirbute olsun.
# knowledge_languages = ['python', 'c#'] class attirbutes
# show_info()
# add_new_languages() yeteneği olsun. Lakin bazen bir dil bazende birden fazla dil gireblisin.
# example input ==> python
# exmaple input ==> python, c#, vb

# class Software_developer():
#     knowledge_languages = []
#
#     def __init__(self, first_name, last_name, knowledge_languages=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.knowledge_languages = []
#         if knowledge_languages:
#             self.add_new_languages(*knowledge_languages)
#
#     def show_info(self):
#         print("First Name:", self.first_name)
#         print("Last Name:", self.last_name)
#         print("Knowledge Languages:", self.knowledge_languages)
#
#     def add_new_languages(self, *languages):
#         for language in languages:
#             langs = language.split(", ")
#             for lang in langs:
#                 self.knowledge_languages.append(lang.lower())
#
#
# developer1 = Software_developer("Ahmet", "Şen", ['python', 'java'])
# languages = input("Enter languages separated by commas: ")
# developer1.add_new_languages(languages)
# developer1.show_info()
#
# developer2 = Software_developer("Ayşe", "Fatma")
# languages = input("Enter languages separated by commas: ")
# developer2.add_new_languages(languages)
# developer2.show_info()

from random import choice


class Character:
    def __init__(self, name: str, race: str, role: str, level: int, weapon: int, armour: int, hp: int):
        self.name = name
        self.race = race
        self.role = role
        self.level = level
        self.armour = armour
        self.hp = hp
        self.weapon = weapon

    def attack(self):
        return self.level * self.weapon

    def defend(self):
        return self.level * self.armour

    def dodge(self):
        print("Player has ben dodged..!")

def main():
    c1 = Character(name="Kara Murat", race="Turk",role='Kahraman', level=100, weapon=100, armour=0, hp=100)
    c2 = Character(name="Kostok", race="Bizans",role='Kral', level=50, weapon=20, armour=100, hp=100)

    while True:
        bot_actions = [c2.attack(), c2.defend(), c2.dodge()]

        bot_action = choice(bot_actions)

        c1_action = input('Type action: ')

        match c1_action:
            case 'attack':
                pass
            case 'defend':
                pass
            case 'dodge':
                pass