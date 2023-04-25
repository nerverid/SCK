# main
import helpers.listHelper
from engine import quiz
from helpers import dateChecker
#from UI import mainWin

def start():
    print("Welcome to system knowledge control")
    #which_start = input("Which the way do you want? Console - 'c', win - 'w': ")
    #if which_start == 'w':
    #    mainWin.start_gui()
    #else:
    check_source()
    con_dialog()
    #print("Bie-bie!")
    
def con_dialog ():
    lHelper = ListHelper()
    newSource = None

    while(True):
        print("""
                    Menu
                1. Work with lists
                2. Testing your self
                q. Exit from programm""")

        print("\n\nYou've got some tests today: ", check_test)
        menu_Chose = input("Enter your chose")
        
        if menu_Chose == "1":
            """Переходим в меню работы со списками"""
            print("""
                    Menu
                1. Create list
                2. Current list
                3. All my list
                q. Exit from programm""")
            talk = yes_no_ask("Do you want to create or read current list (c/r): ")
            if talk == "c":            
                lHelper.create_list()
            elif talk == "r":
                print("You read at the moment: \"The hitchhicker guide to the galaxy\"")
                if check_source():
                    newSource = check_source()
                else:
                    print("Source not found")
            else:
                print("Wrong input")
            """save_result = yes_no_ask("Do you want to save this list? (y/n)")
                if save_result == "y":
                    lHelper.save_list()
                    print(lHelper.display_list())
                else:
                    print(lHelper.display_list())"""
        elif menu_Chose == "2":
            """dateChecker
            получаем текущую дату
            передаём дату в метод с тестами
            тест возвращает список тестов на текущую дату
            Переходим в меню работы с тестами"""
            quiz.start_this()
        elif menu_Chose == "q":
            talk = yes_no_ask("Do you want to exit? (y/n): ")
            if talk == 'y':
                break
            else:
                continue
     
def yes_no_ask(question):
    responce = input(question)
    return responce.lower()

# checking current source, textfile or BD
def check_source():
    print("Нет ничего. Давай создадим что-то новое!")
    return None

# checking tests and return number how many tests for current day
def check_test():
    return 42

def book_download(source):
    book_mask = { "category": "programming",
            "book": [{"book_title": "the hitchhicker's guide to the galaxy",
                      "author":"Douglas Adams", "bookmark": 32}]
            }
    list = fileHelper(source)
    

if __name__ == "__main__":
    start()
