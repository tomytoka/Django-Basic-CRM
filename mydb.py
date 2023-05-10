import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'malolque1',
) 

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE tokco")

print("Done.")