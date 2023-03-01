import sqlite3

connection = sqlite3.connect("database.sl3", 5)
cur = connection.cursor()
#cur.execute("create table users (login text, password text);")
connection.commit()
def register():
    user = input("Ведите логин")
    password = input("Ведите пароль")

    cur.execute(f"select * from users where login = ('{login}')")
    user = cur.fetchone()

    if user:
        print("Пользователь уже сушествует")
    else:
        cur.execute(f"insert into users (login, password) values ('{login}', '{password}')")
        connection.commit()
        print("Користувач успішно зареєстрований")


def login():
       user = input("Ведите логин")
       password = input("Ведите пароль")

       cur.execute(f"select * from users where login= ('{login}')")
       user = cur.fetchone()

       if user and password == user[1]:
           print("Успішний вхід!")
       else:
           print("Неправильний логін або пароль")


def choose_mode():
    mode = input("Виберете режим (1 - Регестрация, 2 - Вход): ")
    if mode == '1':
        register()
    elif mode == '2':
        login()
    else:
        print("Неправильний вибір")






choose_mode()




connection.close()