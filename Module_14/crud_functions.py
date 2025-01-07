import random
import sqlite3

def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    );
    ''')
    for i in range(1, 5):
        cursor.execute(
                'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
            (f'Продукт {i}', f'Описание {i}', i * 100)
                      )
    connection.commit()
    connection.close()

def get_all_products():
    # initiate_db()
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    db = cursor.fetchall()

    connection.commit()
    connection.close()
    return list(db)
