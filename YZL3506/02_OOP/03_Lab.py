# Kalıtım
# Nasıl biyolojide olduğu gibi bizler anne ve babalarımızdan kalıtım vasıtasıyla özellikler kazandıysak yazılımda da üst sınıflar(base class) vasıtasıyla alt sınıflara (child class) özellik aktarabiliyoruz. Buradaki amaç alt sınıfların üst sınıfların ortak özelliklerini bir ata sınıfta toplamasıdır. Kod tekrarını engelleyerek merkezi bir yerden yani atadan özellikler alt sınıflara aktarılabiliyor.Ayrıca üst seviyeli yazılım prensiplerine ve tasarım desenlerine uymak için atılması gereken adımlardan biridir.

# class Human:
#     def __init__(self, height: float, weight: float, alias: str):
#         self.height = height
#         self.weight = weight
#         self.alias = alias
#
#     def show_information(self):
#         return self.__dict__
#
#
# class Knight(Human):
#     pass
#
#
# class Rogue(Human):
#     pass
#
#
# k1 = Knight(height=1.84, weight=98, alias='beast')
# print(k1.show_information())
# r1 = Rogue(height=1.50, weight=65, alias='beast')
# print(r1.show_information())

# Employee objesi için CRUD operasyonları yapalım.
# BaseEntity => Projelerde diğer tüm sınıflara kalıtım veren sınıftır.
from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum

employeees = []


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self, first_name: str, last_name: str, departmant: str):
        self.departmant = departmant
        self.first_name = first_name
        self.last_name = last_name
        self.id = str(uuid4())
        self.status = Status.Active.name
        self.created_at = datetime.now()
        self.created_ip_address = gethostbyname(gethostname())
        self.created_machine_name = gethostname()


class Employee(BaseEntity):
    pass


class Employee_Service:
    def create(self, employee: Employee):
        employee.append(employee)
        print(f'{employee.first_name} {employee.last_name} has been created..!')
    def get_all(self):
        for item in employeees:
            print(f'{item.__dict__}')

    def get_by_full_name(self, full_name: str):
        for employee in employeees:
            if f'{employee.first_name} {employee.last_name}'.lower().__contains__(full_name):
                print(employee.__dict__)

    def get_not_passive(self):
        for employee in employeees:
            if employee.status == 'Active' or employee.status == 'Modified':
                print(employee)

def main():
    service = Employee_Service()
    while True:
        proocess = input('Type process: ')

        match proocess:
            case 'create':
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                departmant = input('Departmant: ')
                employee = Employee(first_name=first_name, last_name=last_name, departmant=departmant)
                service.create(employee)


main()