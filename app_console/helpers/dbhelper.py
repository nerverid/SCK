#DB helper
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="DERgfhjkm1+",
                               database="book_shelf"
                               )

mycursor = mydb.cursor()



def add_list():
    pass

def add_book(db_list, id_book):
    pass

def print_tables():
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print( x)

def create_table(name_table):
    try:
        mycursor.execute("CREATE TABLE %s (name VARCHAR(255), bookList VARCHAR(255))", name_table)
    except:
        print("table created already")

def alter_table():
    try:
        mycursor.execute("ALTER TABLE current_list ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    except:
        print("Something wrong")

def insert_book(n_name, n_booklist, n_table):
    try:
        sql = "INSERT INTO %s (name, bookList) VALUES (%s, %s)"
        val = (n_table, n_name, n_booklist)
        mycursor.execute(sql, val)
    except:
        print("something wrong")

#insert_book("current_list", "1984", "Distopia")


sql = "INSERT INTO current_list (name, bookList) VALUES (%s, %s)"
val = ("1984", "Distopia")
mycursor.execute(sql, val)
#    except:
#        print("something wrong")
mydb.commit()
print(mycursor.rowcount, "record inserted")
