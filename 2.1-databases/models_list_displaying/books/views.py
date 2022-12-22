from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()

    books = {'books':[]}

    for book in book_objects:
        new_book = {
            'name':book.name,
            'author':book.author,
            'pub_date':book.pub_date 
            }
        books['books'].append(new_book)
    
    context = books
    return render(request, template, context)


def show_book(request, date):
    template = 'books/books_date.html'
    book_objects = Book.objects.filter(pub_date=f'{date}')

    books = {'books':[]}

    for book in book_objects:

        new_book = {
            'name':book.name,
            'author':book.author,
            'pub_date':book.pub_date 
            }
        books['books'].append(new_book)
    print (len(books['books']))
    
    context = books

    return render(request, template, context)

