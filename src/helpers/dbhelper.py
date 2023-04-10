#DB helper
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="DERgfhjkm1+")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

for x in mycurcor:
    print(x)
print(mydb)

def add_list():
    pass

def add_book(db_list, id_book):
    pass