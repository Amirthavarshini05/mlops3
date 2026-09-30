books = []

def add_book(book_id, title, price):
    books.append({"id": book_id, "title": title, "price": price})

def display_books():
    for book in books:
        print(book)

def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None

add_book(1, "Python Programming", 500)
add_book(2, "Machine Learning", 700)
display_books()
print(search_book("Python Programming"))
