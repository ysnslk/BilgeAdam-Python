# Crud
# Categories = {}
# Category adında bir sınıfımız olsun. name,description object attirbute olsun.
# Category_service adında bir sınıfımız olsun. Bu sınıf içerisinde CRUD operasyyonlarını yürütürken ihtiyaç duyulan fonksiyonlar yazılır.
# Servisin fonksiyonları => create(), update(), delete(), get_all(), get_by_id()

from uuid import uuid4
from pprint import pprint

categories = {}


class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.id = uuid4()


class Category_Service:
    def create(self, category_obj: Category) -> None:
        categories[str(category_obj.id)] = {
            "name": category_obj.name,
            "description": category_obj.description
        }
        print(f'{category_obj.name} has been created..!')
    def get_all(self, category_dict: dict) -> None:
        pprint(category_dict)

    def get_by_id(self, id: str) -> dict:
        for key in categories:
            if key == id:
                return categories.get(key)

    def update(self, id: str, name: str, description: str):
        category = categories.get(id)
        if category:
            category['name'] = name
            category['description'] = description
            print(f'Category with id {id} has been updated..!')
        else:
            print(f'Category with id {id} does not exist.')

    def delete(self, id: str):
        if id in categories:
            del categories[id]
            print(f'Category with id {id} has been deleted..!')
        else:
            print(f'Category with id {id} does not exist.')



def main():
    service = Category_Service()
    while True:

        process = input("Please type a transaction name: ").lower()

        match process:
            case 'exit':
                print('Application has been closing..!')
                break
            case 'create':
                category_name = input("Category name: ")
                category_description = input("Category description: ")
                category_obj = Category(name=category_name, description=category_description)
                service.create(category_obj)
                service.get_all(categories)
            case 'get all':
                service.get_all(categories)
            case 'get by id':
                id = input("Category id: ")
                pprint(service.get_by_id(id))
            case 'update':
                category_id = input("Category id: ")
                category_name = input("New category name: ")
                category_description = input("New category description: ")
                service.update(category_id, category_name, category_description)
                pprint(service.get_by_id(category_id))
            case 'delete':
                category_id = input("Category id: ")
                service.delete(category_id)
            case _:
                print('Please type a correct transaction name...!')


main()