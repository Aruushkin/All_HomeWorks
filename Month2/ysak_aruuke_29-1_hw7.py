import sqlite3

conn = sqlite3.connect('hw.db')

cursor = conn.cursor()


def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_title TEXT NOT NULL,
                    price REAL NOT NULL DEFAULT 0.0,
                    quantity INTEGER NOT NULL DEFAULT 0
                )''')


def add_product(product_title, price=0.0, quantity=0):
    cursor.execute('''INSERT INTO products (product_title, price, quantity)
                    VALUES (?, ?, ?)''', (product_title, price, quantity))


def update_quantity(product_id, new_quantity):
    cursor.execute('''UPDATE products SET quantity = ?
                    WHERE id = ?''', (new_quantity, product_id))


def update_price(product_id, new_price):
    cursor.execute('''UPDATE products SET price = ?
                    WHERE id = ?''', (new_price, product_id))


def delete_product(product_id):
    cursor.execute('''DELETE FROM products
                    WHERE id = ?''', (product_id,))


def print_all_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)


def print_cheaper_products():
    cursor.execute('''SELECT * FROM products
                    WHERE price < 100.0 AND quantity > 5''')
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_products_by_title(keyword):
    cursor.execute('''SELECT * FROM products
                    WHERE product_title LIKE ?''', ('%' + keyword + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)


create_table()

for i in range(1, 16):
    add_product(f"Товар {i}", i * 10, i)

print("Все товары:")
print_all_products()
print()

update_quantity(1, 20)

update_price(2, 100.0)

print("Товары дешевле 100 сомов и с количеством больше 5:")
print_cheaper_products()
print()

delete_product(3)

print("Все товары после удаления:")
print_all_products()
print()

print("Поиск товаров по названию 'Товар 1':")
search_products_by_title("Товар 1")
print()

conn.commit()
conn.close()

