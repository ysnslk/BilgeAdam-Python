
from pprint import pprint
from requests import get

response = get('https://newsapi.org/v2/everything?q=tesla&from=2024-02-10&sortBy=publishedAt&apiKey=47f3419f49864ca889f632677d485de1')

data = response.json()

# pprint(data)

# print(f'Author: {data["articles"][0]["author"]}')
# print(f'Title: {data["articles"][0]["title"]}')
# print(f'Published Date: {data["articles"][0]["publishedAt"]}')

# Kullanıcıdan yazar ismi alınacak ve bu yazarın makalesi ekrana basılacak
author_name = input('Author Name: ')
for article in data.get('articles'):
    if article.get('author') == author_name:
        pprint(article)


# Free api bulup. Data çekiyoruz. Search mekanizması yapın
# Örneğin BIST data'sı çektiniz. SASA serach edildiğnde ekrana bilgileri basılacak
