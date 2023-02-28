import json

first_book = '{ "category": "programming", "book": [{"book_title": "the hitchhicker\'s guide to the galaxy", "author":"Douglas Adams", "bookmark": 32}]}'

book_dict = json.loads(first_book)
print(book_dict)

def download_file():
    with open('books.json', 'r') as read_f:
        data_f = json.load(read_f)
    print(json.dumps(data_f, indent = 4))

def write_file(f, data_j):
    with open (f, "w") as write_f:
        write_f.write(data_j)

download_file()
f = "newbook.json"
write_file(f, first_book)
