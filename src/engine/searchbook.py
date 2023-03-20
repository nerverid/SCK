#Поиск литературы, составление списка из неё, предварительная сортировка самим модулем файлов по категориям.
import os

path = 'C:\\Users'

print(os.listdir(path))
for i in os.listdir(path):
    print(i)