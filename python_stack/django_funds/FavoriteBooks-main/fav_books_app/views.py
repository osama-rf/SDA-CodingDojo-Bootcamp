from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

#render pages
def index(request):
    return render(request, 'index.html')

def success(request):
    if 'uuid' not in request.session:
        return redirect('/')
    context = {
        'userid' : User.objects.get(id=request.session['uuid']),
        'booklist': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def book_details(request, book_id):
    context = {
        'userid' : User.objects.get(id=request.session['uuid']),
        'details' : Book.objects.get(id=book_id),
        'my_faves': Book.objects.filter(users_who_like=request.session['uuid'])
    }
    return render (request, 'details.html', context)

#redirect pages

#from root route
def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password= pw_hash
        )
        request.session['uuid'] = user.id
    return redirect(f'/books')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['uuid'] = user.id
        return redirect("/books")

#from books main page
def add_a_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/books')
    else:
        uploaded = User.objects.get(id=request.session['uuid'])
        book = Book.objects.create(
            title=request.POST['title'],
            description = request.POST['description'],
            uploaded_by = uploaded,
        )
        this_book = Book.objects.last()
        print(this_book)
        uploaded.liked_books.add(this_book)
    return redirect('/books')

def add_favorite(request, book_id):
    print("this is working")
    this_book = Book.objects.get(id= book_id)
    this_user = User.objects.get(id=request.session['uuid'])
    this_user.liked_books.add(this_book)
    return HttpResponseRedirect (request.META.get('HTTP_REFERER'))

def edit_book(request, book_id):
    errors = Book.objects.book_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return HttpResponseRedirect (request.META.get('HTTP_REFERER'))
    else:
        book_to_update = Book.objects.get(id=book_id)
        book_to_update.title=request.POST['title']
        book_to_update.description = request.POST['description']
        book_to_update.save()
        return HttpResponseRedirect (request.META.get('HTTP_REFERER'))

def unfavorite(request, book_id):
    this_book = Book.objects.get(id= book_id)
    this_user = User.objects.get(id=request.session['uuid'])
    this_user.liked_books.remove(this_book)
    return HttpResponseRedirect (request.META.get('HTTP_REFERER'))

def delete_book(request, book_id):
    to_delete = Book.objects.get(id= book_id)
    to_delete.delete()
    return redirect('/books')

def logout(request):
    request.session.flush()
    return redirect('/')