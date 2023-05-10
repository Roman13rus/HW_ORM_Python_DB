import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables
from functions import jsonparser, get_information_sale_book
import os
from dotenv import load_dotenv
if __name__ == '__main__':
    load_dotenv()
    Login_db = os.getenv('Login_db')
    Password_db = os.getenv('Password_db')
    Name_db = os.getenv('Name_db')
    DSN = f"postgresql://{Login_db}:{Password_db}@localhost:5432/{Name_db}" 
    engine = sqlalchemy.create_engine(DSN) # Создание движка
    create_tables(engine) # создание таблиц
    Session = sessionmaker(bind=engine)
    session = Session() #создание эекземпляра сессии
    session.add_all(jsonparser('text_file.json')) # заполнение таблицы данными из на основе функции jsonparser модуля funktions
    print(f'               название книги            |название магазина| стоимость покупки|      дата покупки') # вывод результатов запроса
    for title, name, price, date_sale in get_information_sale_book(session, {"id": 1}):  #на основе функции get_information_sale_book модуля funktions
        print(f'{title:<40} | {name:<15} | {price:<16} | {date_sale}')
    session.commit()
    session.close()
