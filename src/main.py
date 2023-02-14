# main
from helpers.listHelper import ListHelper

def start():
    print("Welcome to system knowledge control")
    check_source()
    con_dialog()
    print("Bie-bie!")
    
def con_dialog ():
    lHelper = ListHelper()
    while(True):
        talk = yes_no_ask("Do you want to create or read current list (c/r): ")
        if talk == "c":            
            lHelper.create_list()
        elif talk == "r":
            print("You read at the moment: \"The hitchhicker guide to the galaxy\"")
        else:
            print("Wrong input")
        talk = yes_no_ask("Do you want to exit? (y/n): ")
        if talk == 'y':
            save_result = yes_no_ask("Do you want to save this list? (y/n)")
            if save_result == "y":
                lHelper.save_list()
                print(lHelper.display_list())
            else:
                print(lHelper.display_list())
                break
        else:
            continue

def yes_no_ask(question):
    responce = input(question)
    return responce.lower()

def check_source():
    print("Нет ничего. Давай создадим что-то новое!")

start()
