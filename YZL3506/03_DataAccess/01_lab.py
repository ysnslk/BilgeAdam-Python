

# Python Application üzerinden MongoDb veri tabanına erişmek için
from pymongo import MongoClient
from pprint import pprint
import re  # regex modülü

# Connection String oluşturalım ki App Side'tan Server Side erişebilelim
conn = MongoClient('mongodb://localhost:27017')

# Server üzeirnde bir veritabanı yaratalım
db = conn['app_db']

# veri tabanı içerisine bir collection yaratalım
collection = db['products']

# region Insert One Record
# product_name = input('Name: ')
# price = input('Price')
# product = {
#     'name': product_name,
#     'price': price
# }
# result = collection.insert_one(product)
# print(result)
# endregion


# region Insert Many Record
# product_list = [
#     {'_id': 1, 'name': 'Lenova X1 Carbon', 'price': 84.999},
#     {'_id': 2, 'name': 'Macbook Pro M3', 'price': 184.999},
#     {'_id': 3, 'name': 'Asus Zen Book 5', 'price': 144.999},
#     {'_id': 4, 'name': 'Monster Tulpar', 'price': 60.999},
#     {'_id': 5, 'name': 'Monster Alba', 'price': 33.999},
# ]
# collection.insert_many(product_list)
# endregion


# region Read All Record
# for item in collection.find():
#     pprint(item)
# endregion

# region Fiyatı 100'binden fazla olan ürünleri listeleyin
# filter_input = {
#     'price': {
#         '$gt': 100.000
#     }
# }
# for item in collection.find(filter_input):
#     pprint(item)
# endregion


# region Fiyatı 80'ne eşit ve ondan az olan kayıtları listeleyin
# filter_input = {
#     'price': {
#         '$lte': 80.000
#     }
# }
# for item in collection.find(filter_input):
#     pprint(item)
# endregion


# region Fiyatı 60.999 olan ürünü getirin
# filter_input = {
#     'price': {
#         '$eq': 60.999
#     }
# }
# for item in collection.find(filter_input):
#     pprint(item)
# endregion


# region fiyatı 20 bin ile 100 arasında olan ürünleri listeleyin
# query = {
#     '$and': [
#         {'price': {'$gte': 20.000}},
#         {'price': {'$lte': 100.000}}
#     ]
# }
#
# for item in collection.find(query):
#     pprint(item)
# endregion


# region Fiyatı 100 binden az ve ürün adı içerisinde monster geçen ürünleri listeleytin
# query = {
#     'price': {'$lte': 100.000},
#     'name': {'$regex': 'Monster'}
# }
# for item in collection.find(query):
#     pprint(item)
# endregion


# region Baş harfi L olan ürünleri listeleyin
# pattern = re.compile('^L.*')
#
# query = {
#     'name': {'$regex': pattern}
# }
#
# for item in collection.find(query):
#     pprint(item)
# endregion


# region Update
result = collection.update_one(
    # güncellemek istediğimiz kaydı yakalıyoruz
    filter={'name': 'Monster ALba'},
    # yeni değerleri ilgili kayıt alanlarına set ediyoruz.
    update={
        '$set': {
            'name': 'Dell Vega',
            'price': 69.999
        }
    }
)

print(f'{result.modified_count} adet kayıt güncellendi')
# endregion