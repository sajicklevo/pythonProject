import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('my_database.db')


# Устанавливаем соединение с базой данных
# cursor = connection.cursor()

# Создаем таблицу Users
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY,username TEXT NOT NULL,email TEXT NOT NULL,age INTEGER)''')


# Создаем индекс для столбца "email"
# cursor.execute('CREATE INDEX idx_email ON Users (email)')

# Добавляем нового пользователя
# cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

# Обновляем возраст пользователя "newuser"
# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

# Удаляем пользователя "newuser"
# cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

# Выбираем всех пользователей
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()

# Выводим результаты
# for user in users:
#   print(user)

# Выбираем имена и возраст пользователей старше 25 лет
# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
# results = cursor.fetchall()
# for row in results:
#   print(row)

# Получаем средний возраст пользователей для каждого возраста
# cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# Фильтруем группы по среднему возрасту больше 30
# cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
# filtered_results = cursor.fetchall()
# for row in filtered_results:
#     print(row)

# Выбираем и сортируем пользователей по возрасту по убыванию
# cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
# results = cursor.fetchall()
# for row in results:
#   print(row)

# Выбираем и сортируем пользователей по возрасту по убыванию
# cursor.execute('''
# SELECT username, age, AVG(age)FROM Users
# GROUP BY age
# HAVING AVG(age) > ?
# ORDER BY age DESC
# ''', (30,))
# results = cursor.fetchall()
# for row in results:
#   print(row)

# Подсчет общего числа пользователей
# cursor.execute('SELECT COUNT(*) FROM Users')
# total_users = cursor.fetchone()[0]
# print('Общее количество пользователей:', total_users)

# Вычисление суммы возрастов пользователей
# cursor.execute('SELECT SUM(age) FROM Users')
# total_age = cursor.fetchone()[0]
# print('Общая сумма возрастов пользователей:', total_age)

# Вычисление среднего возраста пользователей
# cursor.execute('SELECT AVG(age) FROM Users')
# average_age = cursor.fetchone()[0]
# print('Средний возраст пользователей:', average_age)

# Нахождение минимального возраста
# cursor.execute('SELECT MIN(age) FROM Users')
# min_age = cursor.fetchone()[0]
# print('Минимальный возраст среди пользователей:', min_age)

# Нахождение максимального возраста
# cursor.execute('SELECT MAX(age) FROM Users')
# max_age = cursor.fetchone()[0]
# print('Максимальный возраст среди пользователей:', max_age)

# Находим пользователей с наибольшим возрастом
# cursor.execute('''
# SELECT username, age
# FROM Users
# WHERE age = (SELECT MAX(age) FROM Users)
# ''')
# oldest_users = cursor.fetchall()
# Выводим результаты
# for user in oldest_users:
#   print(user)

# Выбираем всех пользователей
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
# Выводим результаты
# for user in users:
#   print(user)

# Выбираем первого пользователя
# cursor.execute('SELECT * FROM Users')
# first_user = cursor.fetchone()
# print(first_user)
# Выбираем первых 5 пользователей
# cursor.execute('SELECT * FROM Users')
# first_five_users = cursor.fetchmany(5)
# print(first_five_users)
# Выбираем всех пользователей
# cursor.execute('SELECT * FROM Users')
# all_users = cursor.fetchall()
# print(all_users)

# Выбираем всех пользователей
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
# Преобразуем результаты в список словарей
# users_list = []
# for user in users:
#   user_dict = {
#     'id': user[0],
#     'username': user[1],
#     'email': user[2],
#     'age': user[3]
#   }
# users_list.append(user_dict)
# Выводим результаты
# for user in users_list:
#   print(user)

# Выбираем пользователей с неизвестным возрастом
# cursor.execute('SELECT * FROM Users WHERE age IS NULL')
# unknown_age_users = cursor.fetchall()
# Выводим результаты
# for user in unknown_age_users:
#   print(user)

# try:
#     # Начинаем транзакцию
#     cursor.execute('BEGIN')
#
#     # Выполняем операции
#     cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user1', 'user1@example.com'))
#     cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user2', 'user2@example.com'))
#
#     # Подтверждаем изменения
#     cursor.execute('COMMIT')
#
# except:
#     # Отменяем транзакцию в случае ошибки
#     cursor.execute('ROLLBACK')

# Устанавливаем соединение с базой данных
# with sqlite3.connect('my_database.db') as connection:
#     cursor = connection.cursor()

# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# try:
    # Начинаем транзакцию
    # cursor.execute('BEGIN')
    # Выполняем операции
    # cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user1', 'user1@example.com'))
    # cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user2', 'user2@example.com'))
    # Подтверждаем изменения
    # cursor.execute('COMMIT')
# except:
    # Отменяем транзакцию в случае ошибки
    # cursor.execute('ROLLBACK')


# Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# Создаем подготовленный запрос
# query = 'SELECT * FROM Users WHERE age > ?'
# cursor.execute(query, (25,))
# users = cursor.fetchall()
# Выводим результаты
# for user in users:
#   print(user)

# Создаем представление для активных пользователей
# cursor.execute('CREATE VIEW ActiveUsers AS SELECT * FROM Users WHERE is_active = 1')
# Выбираем активных пользователей
# cursor.execute('SELECT * FROM ActiveUsers')
# active_users = cursor.fetchall()
# Выводим результаты
# for user in active_users:
#   print(user)

# Создаем таблицу Users
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# ''')
# Создаем триггер для обновления времени создания при вставке новой записи
# cursor.execute('''
# CREATE TRIGGER IF NOT EXISTS update_created_at
# AFTER INSERT ON Users
# BEGIN
# UPDATE Users SET created_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
# END;
# ''')


# Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# Создаем индекс для столбца "username"
# cursor.execute('CREATE INDEX idx_username ON Users (username)')


# Устанавливаем соединение с базой данных
# connection = sqlite3.connect('tasks.db')
# cursor = connection.cursor()
# Создаем таблицу Tasks
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Tasks (
# id INTEGER PRIMARY KEY,
# title TEXT NOT NULL,
# status TEXT DEFAULT 'Not Started'
# )
# ''')
# Функция для добавления новой задачи
# def add_task(title):
#     cursor.execute('INSERT INTO Tasks (title) VALUES (?)', (title,))
#     connection.commit()
# Функция для обновления статуса задачи
# def update_task_status(task_id, status):
#     cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
#     connection.commit()
# Функция для вывода списка задач
# def list_tasks():
#     cursor.execute('SELECT * FROM Tasks')
#     tasks = cursor.fetchall()
#     for task in tasks:
#         print(task)
# Добавляем задачи
# add_task('Подготовить презентацию')
# add_task('Закончить отчет')
# add_task('Подготовить ужин')
# Обновляем статус задачи
# update_task_status(2, 'In Progress')
# Выводим список задач
# list_tasks()

# Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()