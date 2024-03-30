# Encapsulation (Veri Gizleme)
# Bir sınıfın herhangi bir üyesini encapsulation ettiğmizde, ilgili üyeye ait sınıflardan eriişimi engellemiş oluruz. Bir başka değiş ile ilgili sayfın üyesini erişime kapamış oluyoruz. Bu bağlamda erişemediğimiz üyenin üzerine alt sınıfta değer yazamayız. Lakin belirli şartlar doğrultusunda bu erişimi dolaylı yollar ile yapabiliriz.

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint

class Status(Enum):
    Active = 1,
    Modified = 2,
    Passive = 3

# __ kullandığımızda dışarıya kapalı olduğu anlamına gelir.
class BaseEntity:
    def __init__(self):
        self.__id = ''
        self.__created_date = ''
        self.__created_computer_name = ''
        self.__created_ip_address = ''
        self.__status = ''

    # Not: Double underscore ile tanımladığımız alanlara ne sınıfın örnekleminden (instance) nede bu sınıftan kalıtım alan alt sınıfın örnekleminden erişebiliyoruz. Aşağıda da bir custom function yazarak bu private alanlara değer atadık.

    def set_values_private_attirbute(self):
        self.__id = str(uuid4())
        self.__created_date =datetime.now()
        self.__created_computer_name = gethostname()
        self.created_ip_address = gethostbyname(gethostname())
        self.__status = Status.Active.name
    def show_information(self):
        return self.__dict__
# class Product(BaseEntity):
#     def __init__(self, name: str, price: str):
#         super().__init__()
#         self.name = name
#         self.__price = 0
#         self.__stock = 0
#
#     def set_values_private_attirbute(self, price: float,stock: int):
#         super().set_values_private_attirbute()
#         if price > 0 and stock > 0:
#             self.__price =  price
#             self.__stock = stock
#             print('Product has been created..!')
#             pprint(self.__dict__)
#         else:
#             print('İnvalid input...!\n'
#                   'Product stock and prie can not be negative value or zero')
#
# p1 = Product('Trainning Gloves', 'Everlast training gloves are best ..!')
# p1.set_values_private_attirbute(12.44, 160)***


class Car(BaseEntity):
    def __init__(self,brand :str,model:str):
        super().__init__()
        self.model = model
        self.brand = brand
        self.__price = 0
        self.__sase_no = 0

    def set_value_car_attirbute(self,price):
        if price > 0:
            super().set_values_private_attirbute()
            self.__sase_no = uuid4()
            self.__price = price
            print('Car has been created..!')
            pprint(self.__dict__)

c1 = Car('Dodge','TRX 1500')
c1.set_value_car_attirbute(35.000)