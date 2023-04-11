#DB helper
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="DERgfhjkm1+",
                               database="book_shelf"
                               )

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE current_list (name VARCHAR(255), bookList VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print( x)

def add_list():
    pass

def add_book(db_list, id_book):
    pass
