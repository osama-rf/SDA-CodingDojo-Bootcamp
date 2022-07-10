from django.shortcuts import render, HttpResponse, redirect
from requests import request
from .models import *


def index(request):
    newBook = Book.objects.all()
    context = {
        "newBook": newBook
    }

    return render(request, "index.html", context)


def authors(request):
    newAuthors = Author.objects.all()
    context = {
        "newAuthors": newAuthors
    }

    return render(request, "authors.html", context)


def createBook(request):
    if request.method == 'POST':
        newBooks = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
        )

        newBooks.save()
        return redirect('/')


def createAuthor(request):
    if request.method == 'POST':
        newAuthor = Author.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            notes=request.POST['notes'],
        )
        newAuthor.save()
        return redirect('/authors')


def showBook(request, _id):
    book = Book.objects.get(id=_id)
    authors = Author.objects.all()
    context = {
        "book": book,
        'authors': authors
    }

    return render(request, "books.html", context)


def showAuthor(request, _id):
    author = Author.objects.get(id=_id)

    context = {
        "author": author
    }

    return render(request, "showAuthor.html", context)


def addAuthor(request):
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST["author_id"])

    book.authors.add(author)
    author.books.add(book)

    return redirect(f'/book/{book.id}')

def addBook(request):

    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST["author_id"])

    book.authors.add(author)
    author.books.add(book)

    return redirect(f'/author/{author.id}')

