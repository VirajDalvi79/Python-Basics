import mysql.connector 

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port =3306,
    user = "root",
    password = "Password",
    database = "bank_management"

)
print("Connection Successfull")

cursor = connection.cursor()

cursor.execute("SELECT * FROM ACCOUNTS")
rows = cursor.fetchall()
print(rows)

