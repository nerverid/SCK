#������ �������� �� �������� ������
def create_list(self):
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
    self.grandList.append(newList)

def delete_list(self):
    pass

def edit_list(self):
    pass
    
def save_list(self):
    pass

def import_list(self):
    pass

def export_list(self):
    pass

def display_list(self):
    return self.grandList

def create_record(self):
    pass
    
def delete_record(self):
    pass

def downloa_list(slef):
     pass

