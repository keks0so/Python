import pymysql
import pandas as pd
from config1 import host, user, password, db_name

def sql2csv():

    all_user_name = []
    all_phone = []
    for row in myallData:
        all_user_name.append(row['fio'])
        all_phone.append(row['phone'])

    

    #we need to store this data to CSV
    dic = {'fio' : all_user_name , 
           'phone':all_phone,
    }
    
    df = pd.DataFrame (dic)
    df.to_csv('MySQL/DB.csv')



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

            query = "SELECT fio, phone FROM user"
            cursor.execute(query)
            myallData = cursor.fetchall() 
            
            sql2csv()
            
        
    finally:
        connection.close()
    
except Exception as e:
    print(e)
    print("Подключение не получилось")