# Dünyanın farklı lokasyonlarından kahve çekirdeği ithal edeceğiz.
# Lakin kahve çekirdekilerinin lezzeli ve kalitesi açısından hasat zamanlarına göre ithal edeceğiz.
# 4-7  ay arası Columbia
# 8-11 ay arası Sumatra
# 1 yada 2 yada 12 ay SouthAfrica
# 3. ayda dünyada hasat olmadığı için ithalat işlemi olmayacak.

from abc import ABC, abstractmethod
class BaseService(ABC):
    @abstractmethod
    def ship_from(self) -> str : pass

class SumatraService(BaseService):
    def ship_from(self) -> str:
        return 'from Sumarta'

class ColumbiaService(BaseService):
    def ship_from(self) -> str:
        return 'from Columbia'

class SouthAfricaService(BaseService):
    def ship_from(self) -> str:
        return 'from SouthAfrica'

class DefaultService(BaseService):
    def ship_from(self) -> str:
        return 'shipment not available'

# Bu örnekte Creational Design Pattenrs gruba ait olan factory design patter'i kullandık. Aşağıda shipment method fonksiyonu factory design pattern bize verdiği mantıkta çalışmaktadır.
class Shipment:
    @staticmethod
    def shipment_method(month) -> BaseService:
        if 4 <= month <= 7:
            return ColumbiaService()
        elif 8 <= month <= 11:
            return SumatraService()
        elif month == 1 or month == 12 or month == 2:
            return SouthAfricaService()
        else:
            return DefaultService()

def main():
    for month in range(1, 13):
        product_shipment = Shipment.shipment_method(month)
        print(f'Coffe beans shipment {product_shipment.ship_from()}')

main()