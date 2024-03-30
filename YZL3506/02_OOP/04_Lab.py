# Method Overriding
# Ata sınıflarda(parent class) bulunan methodların alt sınıflarda ezilerek onlara yeni işlevler kazandırılmasına method overriding diyoruz. Ata sınıftan gelen fonksiyonun illa var olan yeteneğini geçerisiz kılıp ona yeni yetenek kazandırmaya gerek yoktur. Bazen var olan yetenek extend edilebilir.

# from uuid import uuid4
# from datetime import datetime
# from socket import gethostname, gethostbyname
# from enum import Enum
# from pprint import pprint
#
#
# class Status(Enum):
#     Active = 1
#     Modified = 2
#     Passive = 3
#
#
# class BaseEntity:
#     def __init__(self, name: str, description: str):
#         self.name = name
#         self.description = description
#         self.id = str(uuid4())
#         self.status = Status.Active.name
#         self.created_at = datetime.now()
#         self.created_ip_address = gethostbyname(gethostname())
#         self.created_machine_name = gethostname()
#
#     def show_info(self):
#         print(f'Id: {self.id}\n,'
#               f' Name: {self.name}\n'
#               f'Description: {self.description}\n')
#
# class Category(BaseEntity):
#     pass
#
# class Product(BaseEntity):
#     def __init__(self,name: str,description: str, price: float, stock: float):
#         super().__init__(name,description)
#         self.stock = stock
#         self.price = price
#
#     def show_info(self):
#         super().show_info()
#         print(f'Stock: {self.stock}\n'
#               f'Price: {self.price}')
#
# c1 = Category('Boxing Gloves', 'Best Boxing Gloves')
# c1.show_info()
# p1 = Product('Training Gloves', 'Best Trainning Gloves', 12.2, 34)
# p1.show_info()

# BasePhone adında bir ata sınıf oluşturalım. phone_id, brand model, price attirbute'leri olsun
# show_info fonksiyonu olsun. phone_ring_sound() fonksiyonu 'genel telefon sesi' string ifadesi retur
# samsung adında bir sınıf olsun. BasePhone kalıtım olacak. operatin_system attirbute olsun. phone_ring_sound() ' samsung telefon sesi return etsin.
# Iphone adında bir sınıf oluşturalım. BasePhone kalıtım alacak. Camera attirbute olsun. phone_ring_sound(= 'iphone telefon sesi' return etsin.
# Huaweie adında bir sınıf oluşturalım. BasePhone kalıtım alacak. Anten attirbute olsun. phone_ring_sound() 'huaweie telefon sesi return etsin.

# class BasePhone:
#     def __init__(self, phone_id, brand, model, price):
#         self.phone_id = phone_id
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def show_info(self):
#         print(f"Phone ID: {self.phone_id}")
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Price: {self.price}")
#
#     def phone_ring_sound(self):
#         return 'Genel telefon sesi'
#
#
# class Samsung(BasePhone):
#     def __init__(self, phone_id, brand, model, price, operating_system):
#         super().__init__(phone_id, brand, model, price)
#         self.operating_system = operating_system
#
#     def phone_ring_sound(self):
#         return 'Samsung telefon sesi'
#
#
# class Iphone(BasePhone):
#     def __init__(self, phone_id, brand, model, price, camera):
#         super().__init__(phone_id, brand, model, price)
#         self.camera = camera
#
#     def phone_ring_sound(self):
#         return 'iPhone telefon sesi'
#
#
# class Huawei(BasePhone):
#     def __init__(self, phone_id, brand, model, price, anten):
#         super().__init__(phone_id, brand, model, price)
#         self.anten = anten
#     def phone_ring_sound(self):
#         return 'Huawei telefon sesi'
#
#
# samsung_phone = Samsung(phone_id=1, brand="Samsung", model="Galaxy S21", price=1500, operating_system="Android")
# iphone_phone = Iphone(phone_id=2, brand="Apple", model="iPhone 13", price=1800, camera="Dual")
# huawei_phone = Huawei(phone_id=3, brand="Huawei", model="Mate 40", price=1200, anten="5G")
#
# samsung_phone.show_info()
# print(samsung_phone.phone_ring_sound())
#
# iphone_phone.show_info()
# print(iphone_phone.phone_ring_sound())
#
# huawei_phone.show_info()
# print(huawei_phone.phone_ring_sound())

# BaseBill sınıfımız olsun. bill_name, value_add_task, amount attirbute sahip olsun. calculate_bill ve create_log fonsiyoları olsun.
# log'lar bill_info.txt dosyasına yazılsın. bill_name ve total_amount yazmanız ve tarih yeterli
# calculate_bill() amount *  value_add_task
# Water_Bill , Electricity_Bill, Natural_Gas_Bill child classes
# su faturasının mill adında bir özelliği olsun.
# elektrik kw adında bir özelliği olsun.
# doğalcaz m3 adında bir özelliği olsun.

from datetime import datetime

class BaseBill:
    def __init__(self, bill_name, value_add_task, amount):
        self.bill_name = bill_name
        self.value_add_task = value_add_task
        self.amount = amount

    def calculate_bill(self):
        return self.amount * self.value_add_task

    def create_log(self):
        with open("bill_info.txt", "a") as f:
            f.write(f"{self.bill_name} - Total Amount: {self.calculate_bill()} - Date: {datetime.now()}\n")


class WaterBill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount, mill):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill


class ElectricityBill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount, kw):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw


class NaturalGasBill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount, m3):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3


water_bill = WaterBill(bill_name="Water Bill", value_add_task=2, amount=100, mill=50)
electricity_bill = ElectricityBill(bill_name="Electricity Bill", value_add_task=0.5, amount=200, kw=100)
natural_gas_bill = NaturalGasBill(bill_name="Natural Gas Bill", value_add_task=1.5, amount=150, m3=80)

print(water_bill.calculate_bill())
print(electricity_bill.calculate_bill())
print(natural_gas_bill.calculate_bill())

water_bill.create_log()
electricity_bill.create_log()
natural_gas_bill.create_log()
