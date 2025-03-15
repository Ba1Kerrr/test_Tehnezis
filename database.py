import sqlite3
conn = sqlite3.connect('test.db')

cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        title TEXT,
        url TEXT,
        xpath TEXT
    )
               ''')

def add_data(title, url, xpath):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (title, url,xpath) VALUES ('{title}', '{url}','{xpath}')")
    conn.commit()

# Сохраняем изменения
def take_data():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # Выводим записи из таблицы
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

conn.close()
#этот код для того чтобы работать с бд