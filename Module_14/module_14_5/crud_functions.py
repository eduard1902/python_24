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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NON NULL,
    balance INTEGER NOT NULL DEFAULT 1000);
    ''')

    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (username, email, age))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    user_chek = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if user_chek.fetchone() is None:
        return False
    else:
        return True
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    db = cursor.fetchall()

    connection.commit()
    connection.close()
    return list(db)
# initiate_db()