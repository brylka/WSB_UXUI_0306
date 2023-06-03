import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='xxx'
)

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM users")

    records = cursor.fetchall()

for record in records:
    id, name, surname, email = record
    print(f"ID: {id}, Imię: {name}, Nazwisko: {surname}, Email: {email}")