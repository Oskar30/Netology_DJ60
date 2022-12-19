from books.models import Book

book_objects = Book.objects.all()

for el in book_objects:
    print(el)

