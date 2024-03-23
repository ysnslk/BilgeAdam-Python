# Python programlama dilinde bir nesne yaratmak için class anahtar sözcüğünü kullanıyoruz. class ile tanımalddığımız yapı içerisnde yaratacağımız ya da projemizde ihtiyaç duyduğumuz (objenin) özelliklerini tanımlıyoruz. Class'ları gerçek dünyada ki prototiplere benzetebiliriz.

class Vehicle:
    # Attirbute (özellikleri) tanımladık.
    door_number = 0
    brand = ''
    model = ''
    engine_size = ''
    torque = 0

# Aşağıda Vehicle() sınıfından bir nesne ürettik.Yazılım dünyasında buna çıkartma (instance) denir.
x = Vehicle()
x.brand = 'Mercedes'
x.model = 'C'
x.engine_size = 5
x.torque = 4
print(f'Brand: {x.brand}')

# Artık istediğimiz yerde istediğimiz kadar Vehicle() sınmıfıdan nesne üretebiliriz. Nasıl ki built-in nesnesini istediğimiz yerde istediğimiz kadar kullanabiliyorsak custom nesneler içinde geçerlidir.

y = Vehicle()
y.brand = 'Ford'
y.model = 'Shellby'
y.door_number = 4
y.engine_size = 6
y.torque = 5
print(f'Brand: {y.brand} '
      f'Model: {y.model} '
      f'Door number: {y.door_number} '
      f'EngineSize: {y.engine_size} '
      f'Torque: {y.torque}')

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

class Departman:
    department_name = ''
    employee_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Departman.employee_count += 1
        print("Employee count increased to", Departman.employee_count)

    def show_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Departmant:",self.department_name)

    def show_employee_count(self):
        print("Total Employee count:", self.employee_count)

employee1 = Departman("Ali", 30)
employee2 = Departman("Veli", 25)
employee3 = Departman("Yasin", 28)

employee1.show_information()
employee2.show_information()
employee3.show_information()


