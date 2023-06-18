import sqlite3

conn = sqlite3.connect('../hw.db')
cursor = conn.cursor()

# price = цена
# products_title = название
# quantity = количество


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR(200) NOT NULL,
        price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')

conn.commit()

def add_products():
    products = [
        ('Жидкое мыло с запахом ванили', 50, 10),
        ('Мыло детское', 49.99, 5),
        ('Шампунь для волос', 129.99, 15),
        ('Зубная паста', 79.99, 8),
        ('Мыло жидкое антибактериальное', 79.99, 12),
        ('Крем для лица', 199.99, 3),
        ('Дезодорант', 89.99, 20),
        ('Шампунь для окрашенных волос', 149.99, 6),
        ('Маска для волос', 79.99, 10),
        ('Крем для рук', 59.99, 25),
        ('Мыло туалетное', 29.99, 30),
        ('Бальзам для губ', 39.99, 15),
        ('Лосьон', 149.99, 5),
        ('Кондиционер для волос', 99.99, 8),
        ('Зубная нить', 25.99, 40),
    ]

    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()
# update = обновлять
# insert = вставить в
# select = выбирать
def update_quantity(product_id, new_quantity):
        cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
        conn.commit()

def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()

def print_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(f'ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}')

def print_cheap_products():
    cursor.execute('SELECT * FROM products WHERE price < 100.0 AND quantity > 5')
    products = cursor.fetchall()
    for product in products:
        print(f'ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}')


def search_products_by_title(name):
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + name + '%',))
    product = cursor.fetchall()
    for product in product:
        print(f'ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}')

add_products()
print("Добавленные товары:")
print_all_products()
print()

update_quantity(3, 20)
print("Товар с измененным количеством:")
print_all_products()
print()

update_price(5, 59.99)
print("Товар с измененной ценой:")
print_all_products()
print()

delete_product(2)
print("Удаленный товар:")
print_all_products()
print()

print("Товары с ценой ниже 100 сомов и количеством больше 5:")
print_cheap_products()
print()

print("Результат поиска по названию:")
search_products_by_title('мыло')




