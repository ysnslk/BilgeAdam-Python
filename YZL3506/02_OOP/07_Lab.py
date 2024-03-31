from abc import ABC, abstractmethod
from datetime import datetime


# Not: Artık nesnelerimizi temsil eden sınıfların içerisinde CRUD operasypnlarını yazmıyoeuz. Nesne farklı bir sınıf crud operasyonlarını içeren foksiyonlar ise fgrklı bir sınıf olacak. Bu bağlamda la_04 fatura örneğini yujarıdaki mantığa göre bidaha yapalım.

class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.amount = amount
        self.value_add_task = value_add_task
        self.bill_name = bill_name


class ElectrictyBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw


class WaterBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: float):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill


class NaturelGasBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3


class BaseService(ABC):
    @abstractmethod
    def calculate_bill(self, bill: BaseBill) -> float: pass

    def create_log(self, bill:BaseBill, result: float) -> None:
        with open(file='lab_07_bill_info.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Bill Name: {bill.bill_name} || '
                       f'Total Amount: {result} || '
                       f'Create Date: {datetime.now()}\n')


class WaterBillService(BaseService):
    def calculate_bill(self, bill: WaterBill) -> float:
        return bill.amount * bill.value_add_task * bill.mill

class ElectricityBillService(BaseService):
    def calculate_bill(self, bill: ElectrictyBill) -> float:
        return bill.amount * bill.value_add_task * bill.kw


class NaturelGasBillService(BaseService):
    def calculate_bill(self, bill: NaturelGasBill) -> float:
        return bill.amount * bill.value_add_task * bill.m3


water_bill = WaterBill('ISKI', 12.3 ,34.5,56.7)
water_service = WaterBillService()
result = water_service.calculate_bill(water_bill)
water_service.create_log(water_bill, result)

electricity_bill = ElectrictyBill('OEDAS', 12.3 ,34.5,56.7)
electricity_service = ElectricityBillService()
result = electricity_service.calculate_bill(electricity_bill)
electricity_service.create_log(electricity_bill, result)

naturel_gas_bill = NaturelGasBill('Esgaz', 12.3 ,34.5,56.7)
naturel_gas_service = NaturelGasBillService()
result = naturel_gas_service.calculate_bill(naturel_gas_bill)
naturel_gas_service.create_log(naturel_gas_bill, result)