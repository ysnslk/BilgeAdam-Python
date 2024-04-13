

from pymongo import MongoClient
from models import Category


# region Connect to MongoDB
conn = MongoClient('mongodb://localhost:27017')

db = conn['CRUD_db']

collection = db['categories']
# endregion


# region Seed Data
# Proje ilk çalıştırıldığında veri tabanı yaratılırken burada ki oluşturaln koleksiyon ile yani data ile yaratılmasına diyoruz.
# Bize sağladığı avantaj örneğin hemen reqd operasyonlarını hızlıca yaza biliriz. bir tane user yaratılmışsa login olunup belirli testler yapılabilinir vs vs
# Uyarı: bu bloktaki kodları bir kez çalıştırdıktan sonra yoruma alın
# categories = [
#     Category('Boxing Gloves', 'Everlast produce best boxing gloves').__dict__,
#     Category('Punching Bags', 'Everlast produce best punching bags').__dict__,
#     Category('Protective Equipment', 'Everlast produce best protective equiment').__dict__,
# ]
#
# collection.insert_many(categories)
# endregion