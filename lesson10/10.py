import sqlite3

connection = sqlite3.connect("database.sl3", 5)
cur = connection.cursor()

#cur.execute("create table users (id int primary key not null, login text, password text);")
#cur.execute("insert into users ( id, login, password) values ( 2, 'dbr', 'pass1');")
#cur.execute("insert into users ( id, login, password) values ( 3, 'viva', 'videli');")
#cur.execute("insert into users ( id, login, password) values ( 4, 'mika', 'yoyo');")
#cur.execute("insert into users ( id, login, password) values ( 5, 'sobaka', 'werty');")
cur.execute("select password from users where login='dbr';")
cur.execute("select password from users where login='viva';")
cur.execute("select password from users where login='mika';")
cur.execute("select password from users where login='sobaka';")
cur.execute("select password from users where login='user1';")
connection.commit()
res = cur.fetchall()
print(res)
#print(connection)
#print(cur)

connection.close()