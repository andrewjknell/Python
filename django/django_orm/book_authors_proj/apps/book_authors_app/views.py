from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from .models import Author 


def books(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request,'book_authors_app/books.html', context)


def authors(request):
    context = {
        'authors': Author.objects.all(),
       
    }
    return render(request, 'book_authors_app/authors.html',context)


def show_author(request, get_id):
    context = {
        'author': Author.objects.get(id = get_id),
        'add_book': Book.objects.all(),
    }
    return render(request, 'book_authors_app/show_author.html',context)


def show_book(request, get_id):
    context = {
        'book': Book.objects.get(id = get_id),
        'add_author': Author.objects.all(),
    }
    return render(request,'book_authors_app/show_book.html',context)


def add_book(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['new_title'],desc=request.POST['new_desc'])
    return redirect('/books')


def add_author(request):
    if request.method == 'POST':
        Author.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],notes=request.POST['notes'])
    return redirect('/authors')


def book_add_author(request, book_id):
    if request.method == 'POST':
        author_id = request.POST['new_author']
        new_author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=book_id)
        book.authors.add(new_author)
    return redirect('/books/'+ book_id)
        

def author_add_book(request, author_id):
    if request.method == 'POST':
        book_id = request.POST['new_book']
        new_book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=author_id)
        author.books.add(new_book)
    return redirect('/authors/'+ author_id)