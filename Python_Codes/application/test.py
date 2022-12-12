import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="root", database='english_excel')
print(connection)
cursor = connection.cursor()
res = cursor.execute("SELECT email FROM users WHERE email = 'admin@admin.co';")
print(type(res))
# print(cursor.execute('SELECT * FROM db;'))
# print(cursor.fetchall())
# some other statements  with the help of cursor
# cursor.execute(f"INSERT INTO users VALUES (0, 'admin3', 'admin3', 'admin@admin.com', 'adminadmin_123');")
# connection.commit()
# connection.close()
