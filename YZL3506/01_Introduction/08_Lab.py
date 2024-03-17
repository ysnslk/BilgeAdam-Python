from uuid import uuid4

# Dictionary (Sözlük)

# Sözlük, list tuple gibi bir başka verileri depoladığımız yapıdır.
# Sözkülker anahtar & değer (key & value) mantığında çalışırlar

my_dict = {
    'Full Name': 'Burak Yılmaz',
    'Age': 34,
    'Interested Sport': ['Boxing', 'Wrestling', 'UFC'],
    'Favorite Books': {
        'War History': 'Cambridge War History',
        'Scientific:':{
            'Karl Poper': 'The Logic Scientific Discovery'
        }
    }
}

release_year_movie = {
    'Fight Clup': 1999,
    'The Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2010,
    'Dune': 2011
}

# Herhangi bir value ekrana basın
# Yol I
# print(f'Interstellar Release: {release_year_movie["Interstaller"]}')
# # Yol II
# print(f'Interstellar Release: {release_year_movie.get('Interstaller')}')

# print(release_year_movie.items())
# for key, value in release_year_movie.items():
#     print(f'Movie Name: {key}\n'
#           f'Release Year: {value}')
#
# my_family = [
#     ('Burak Yılmaz', 35, 'beast'),
#     ('Hakan Yılmaz', 38, 'bear'),
#     ('İpek Yılmaz', 40, 'keko'),
# ]
#
# for x,y,z in my_family:
#     print(f'Full Name: {x}\n'
#           f'Age: {y}\n'
#           f'Alias: {z}')

# CRUD (Create-Read-Update-Delete)
products = [
    {'name': 'Everlast Pro Boxing Gloves', 'price': 245},
    {'name': 'Everlast Training Gloves', 'price': 200},
    {'name': 'Everlast Heavy Bag', 'price': 445},
    {'name': 'Iphone 15 Pro Max', 'price': 85000},
    {'name': 'Samsung S24 Ultra', 'price': 80000},
    {'name': 'Lenovo X1 Carbon', 'price': 59000},
]

# products listesindeki tüm ürünlerin fiyatlarını toplayarak ekrana basın
# priceAll = 0
# for product in products:
#     priceAll = priceAll + product['price']
#
# print(priceAll)


# products listesinde ki ürünlerin fiyatı 30000 den buyuk olanlarlı listeleyin
# for product in products:
#     if product.get('price') > 30000:
#         print(f'{product.get('name')} : {product.get("price")}')

# ürün adı içerisinde Everlast geçen ve fiyat aralığı 240 ile 500 arasında olan ürünleri listeleyiniz.
# for product in products:
#     if 'Everlast' in product['name'] and 240 < product['price'] < 500:
#         print(f'{product.get('name')} : {product.get("price")}')

# Boş bir students sözlüğü yaratalım
# Dictionary Structure
# students
# students = {
#     'student_id': {
#         'first_name': 'fdasa',
#         'last_name': 'fdfds',
#         'phone': '256254512',
#     },
#     'student_id': {
#         'first_name': 'fdasa',
#         'last_name': 'fdfds',
#         'phone': '256254512',
#     }
# }

# öğrenci id'lerini uuid4 ile yaratın
students = {}

while True:
    print('Manuel Guide \n'
          '===============\n'
          'Create\n'
          'Update\n'
          'Delete\n'
          'Exit')
    process = input('Type your process upon manuel guide: ').lower()

    match process:
        case 'create':
            pass
        case 'list':
            pass
        case 'update':
            pass
        case 'delete':
            pass
        case _:
            print('Please type  valid process name ..!')
student_id = str(uuid4())
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
phone = input('Enter your phone number: ')

students[student_id] ={
    'first_name': first_name,
    'last_name': last_name,
    'phone': phone
}
print(students)

