from abc import ABC, abstractmethod

from settings import collection
import pymongo
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId
from pprint import pprint


class BaseService(ABC):
    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, pk): pass

    @abstractmethod
    def update(self, filter_value: dict, set_value: dict): pass


class CategoryService(BaseService):
    def create(self, item: dict):
        try:
            collection.insert_one(item)
            print(f'{item["name"]} is created!')
        except PyMongoError as err:
            print(err.__doc__)

    # region Read Operations
    def get_all(self):
        # Status Active veye Modified Durumda olan kayıtları listeleyin
        query = {
            '_BaseEntity__stats': {
                '$in': ['Active', 'Modified']
            }
        }

        projection = {
            '_id': 0,
            'name': 1,
            'description': 1
        }

        for item in collection.find(query, projection).sort('name', pymongo.ASCENDING):
            pprint(item)

    def get_by_id(self, pk):
        query = {
            '_id': ObjectId(pk),
            '_BaseEntity__stats': {
                '$in': ['Active', 'Modified']
            }
        }

        # Sorgu sonucunda dönen sonuç kümesinde hangi alanların gösterilmeisni istiyorsak alan adı : 1 kullanırken gösterilmesini istemediğimiz alnalara 0 veriyoruz.
        projection = {
            '_id': 0,
            'name': 1,
            'description': 1
        }

        # sort() fonksiyonunda sıralama yaparken default Ascending'tir
        for item in collection.find(query, projection).sort('name'):
            pprint(item)
    # endregion

    def update(self, filter_value: dict, set_value: dict):
        try:
            result = collection.update_one(
                filter_value,
                {
                    '$set': set_value
                }
            )

            print(f'{result.modified_count} amount record has been effected..!')
            pprint(self.get_by_id(filter_value['_id']))
        except PyMongoError as err:
            print(err.__doc__)
