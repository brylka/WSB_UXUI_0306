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
    #print(f"ID: {id}, Imię: {name}, Nazwisko: {surname}, Email: {email}")
    print(f"ID: {id:>3} Imię: {name:<15} Nazwisko: {surname:<15} Email: {email:<30}")
