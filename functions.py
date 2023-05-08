import json
from models import Publisher, Book, Shop, Stock, Sale 
def jsonparser(files):  # Функция получения данных из json файла(для заполнения БД) возвращает список экземпляров классов наших объектов с параметрами в соответствии с моделями 
    with open(files) as file:
        r = json.load(file)
    object_list = []
    for data in r:
        if data["model"] == 'publisher':
            publishers = Publisher(name = data["fields"]["name"])
            object_list.append(publishers)
        elif data["model"] == 'book':
            books = Book(title = data["fields"]["title"], id_publisher = data["fields"]["id_publisher"])
            object_list.append(books)
        elif data["model"] == 'shop':
            shops = Shop(name = data["fields"]["name"])
            object_list.append(shops)
        elif data["model"] == 'stock':
            stocks = Stock(id_shop = data["fields"]["id_shop"], id_book = data["fields"]["id_book"], count = data["fields"]["count"] )
            object_list.append(stocks)
        elif data["model"] == 'sale':
            sales = Sale(price = data["fields"]["price"], date_sale = data["fields"]["date_sale"], id_stock = data["fields"]["id_stock"], count = data["fields"]["count"] )
            object_list.append(sales)
    return object_list

def get_information_sale_book(connection ,publish:dict) -> str: # функция получения информации из БД (в соответствии с заданием), на вход принимает:сессию для подключения и словарь(параметр(id или name): значение параметра)
    query = connection.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)
    if publish.keys() == 'name':
        query = query.filter(Publisher.name == publish['name'])
    elif publish.keys() == 'id':
        query = query.filter(Publisher.id == publish['id'])
    return query.all()
    




