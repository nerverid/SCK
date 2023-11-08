#Поиск литературы, составление списка из неё, предварительная сортировка самим модулем файлов по категориям.
import os

path = 'C:\\Users\\Администратор'

txt_list = list()
pdf_list = list()
djvu_list = list()
fb2_list = list()

def search_books(path, level=1):
    #print('Level=', level, 'Content: ', os.listdir(path))
    try:
        for i in os.listdir(path):
            #print(i)
            if 'txt' in i[-3:]:
                print(i, " I've found it! It's TXT")
                txt_list.append(i)
            elif 'fb2' in i[-3:]:
                print(i, " I've found it! It's fb2")
                fb2_list.append(i)
            elif 'pdf' in i[-3:]:
                print(i, " I've found it! It's pdf")
                pdf_list.append(i)
            elif 'djvu' in i[-4:]:
                print(i, " I've found it! It's djvu")
                djvu_list.append(i)
        for i in os.listdir(path):
            if os.path.isdir(path+'\\'+i):
                #print("Step down: ", path+'\\'+i )
                search_books(path+'\\'+i , level+1)
                #print ("Go to", path)                
    except Exception:
        print("Access Denided")

search_books(path)
print(txt_list)
print(pdf_list)
print(djvu_list)
print(fb2_list)
