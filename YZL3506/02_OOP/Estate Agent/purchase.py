from property import Property, House, Apartment
class Purchase(Property):
    def __init__(self,price='',taxes='',*args,**kwargs):
        super().__init__()
class ApartmantPurchase(Apartment, Purchase):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)

class HousePurchase(House, Purchase):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)
