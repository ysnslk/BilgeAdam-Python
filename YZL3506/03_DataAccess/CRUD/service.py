

from abc import ABC, abstractmethod

import pymongo

from settings import collection
from pymongo.errors import ProtocolError
from bson.objectid import ObjectId
from pprint import pprint


class BaseService(ABC):
    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, pk): pass


class CategoryService(BaseService):
    def create(self, item: dict):
        pass

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
        for item in collection.find(query,  projection).sort('name'):
            pprint(item)
    # endregion
