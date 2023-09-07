import pymysql
from config1 import host, user, password, db_name
import argon2


fio = 'Неденис Непирогов Невладимирович'
email = 'moonlion@tut.by'
password1 = 'lkiop098'
phone = '+375296769046'


password2 = password1.encode("utf-8")
hasher = argon2.PasswordHasher()
hashed_password = hasher.hash(password2)

try:
    connection = pymysql.connect(
    host = host,
    port = 3306,
    user = user,
    password = password,
    database = db_name,
    cursorclass = pymysql.cursors.DictCursor
    )
    print("Успех")
    print("#" * 20)

    try:
        
        
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO user (fio, email, password, phone) VALUES (%s, %s, %s, %s);" 
            cursor.execute(insert_query, (fio, email, hashed_password, phone))
            connection.commit()
        
    finally:
        connection.close()
    
except Exception as e:
    print(e)
    print("Подключение не получилось")
