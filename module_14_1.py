import sqlite3

# Создание базы данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
# Создание полей
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# Заполнение 10-ю записями
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', 1000))

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500
cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500,))

# Удаляем каждую 3ую запись в таблице начиная с 1ой
count = 1
while count < 11:
    cursor.execute("DELETE FROM Users WHERE username = ? ", (f'User{count}',))
    count += 3

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя:{user[0]}| Почта: {user[1]}| Возраст: {user[2]}| Баланс: {user[3]}')

connection.commit()
connection.close()
