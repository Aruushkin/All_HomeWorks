import sqlite3


conn = sqlite3.connect('../database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')


cursor.execute("INSERT INTO countries (title) VALUES ('Кыргызстан')")
cursor.execute("INSERT INTO countries (title) VALUES ('Германия')")
cursor.execute("INSERT INTO countries (title) VALUES ('Корея')")
cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")
cursor.execute("INSERT INTO countries (title) VALUES ('Франция')")
cursor.execute("INSERT INTO countries (title) VALUES ('Нидерланды')")
cursor.execute("INSERT INTO countries (title) VALUES ('Италия')")


cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    )
''')

cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Бишкек', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Бердин', 2)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Сеул', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Пекин', 4)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Париж', 5)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Амстердам', 6)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Рим', 7)")


cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities (id)
    )
''')

cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Николас', 'Кейдж', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Элтон', 'Джон', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Мэг', 'Райан', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Чарли', 'Шин', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Смит', 'Уилл', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Бред', 'Питт', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Мэган', 'Фокс', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Джэйми', 'Фокс', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Тоби', 'Магваер', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Том', 'Холланд', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Анджелина', 'Джоли', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Эмма', 'Вотсан', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Гарри', 'Поттер', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Рон', 'Уизли', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Гермиона', 'Грэйнжер', 1)")


conn.commit()
conn.close()


print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")


conn = sqlite3.connect('../database.db')
cursor = conn.cursor()
cursor.execute("SELECT title FROM cities")
cities = cursor.fetchall()
conn.close()

print("Список городов:")
for city in set(cities):
    print(city[0])


while True:
    city_id = input("Введите id города (для выхода введите 0): ")
    if city_id == '0':
        break


    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT employees.first_name, employees.last_name, countries.title, cities.title
        FROM employees
        INNER JOIN cities ON employees.city_id = cities.id
        INNER JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (city_id,))

    employees = cursor.fetchall()
    conn.close()


    if len(employees) == 0:
        print("Нет сотрудников в данном городе.")
    else:
        print("Сотрудники в выбранном городе:")
        for employee in set(employees):
            print("Имя:", employee[0])
            print("Фамилия:", employee[1])
            print("Страна:", employee[2])
            print("Город:", employee[3])
            print()
