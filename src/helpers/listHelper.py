#������ �������� �� �������� ������
self.grandList = []

def create_list():
    print("Here some very important dialog, how create list about")
    newList = []
    while(True):
        ext = input("Do you want add new record (y/n)")
        if ext == 'y':
            print("Please. Add new record")
            title = input("Enter title: ")
            author = input("Enter author: ")
            newRecord = [title, author]
            newList.append(newRecord)
        else:
            break
    grandList.append(newList)

def delete_list(val_list):
    

def edit_list():
    pass

def save_list():
    pass

def import_list():
    pass

def export_list():
    pass

def display_list():
    return grandList

def create_record():
    pass

def delete_record():
    pass

def downloa_list():
    pass

def simple_test_this_module():
    book = { "category": "programming",
             "book": [{"book_title": "the hitchhicker's guide to the galaxy",
                       "author":"Douglas Adams",
                       "bookmark": 32}]}
    

simple_test_this_module()
