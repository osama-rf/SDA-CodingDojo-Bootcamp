from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
import bcrypt

from .models import User, Author, Book, Review


# Create your views here.
def login_reg_page(request):
    return render(request, 'login_reg.html')


def create_user(request):
    # potential_users = User.objects.filter(email = request.POST['email'])

    # if len(potential_users) == 0:
    #     messages.error(request, "User with that email already exists!")
    #     return redirect('/')

    # errors = User.objects.basic_validator(request.POST)

    # if len(errors) > 0:
    #     for key, val in errors.items():
    #         messages.error(request, val)
    #     return redirect('/')

    # hashed_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        alias = request.POST['alias'],
        birthday = request.POST['birthday'],
        email = request.POST['email'],
        # password = hashed_pw,
    )

    request.session['user_id'] = new_user.id

    return redirect('/books')


def login(request):
    potential_users = User.objects.filter(email = request.POST['email'])

    if len(potential_users) == 0:
        messages.error(request, "Please check your email and password.")
        return redirect('/')

    user = potential_users[0]

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Please check your email and password.")
        return redirect('/')

    request.session['user_id'] = user.id

    return redirect('/books')


def books_page(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')
        
    current_user = User.objects.get(id=request.session['user_id'])
    all_reviews = Review.objects.all()
    last_three_reviews = all_reviews.order_by('-created_at')[:3]
    # books_with_reviews = Book.objects.filter(reviews__isnull = False).distinct()
    books_with_reviews = Book.objects.exclude(reviews = None)

    context = {
        'current_user': current_user,
        'all_reviews': all_reviews,
        'last_three_reviews': last_three_reviews,
        'books_with_reviews': books_with_reviews
    }

    return render(request, 'books.html', context)

def add_book_page(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')
        
    current_user = User.objects.get(id=request.session['user_id'])
    all_authors = Author.objects.all().order_by('full_name')

    context = {
        'current_user': current_user,
        'all_authors': all_authors
    }

    return render(request, 'add_book.html', context)

def create_book(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')

    current_user = User.objects.get(id=request.session['user_id'])

    if request.POST['author_select'] == "none" and request.POST['author_text'] == "":
        messages.error(request, "Author is required!")
        return redirect('/books/add')
    if request.POST['author_select'] != "none" and request.POST['author_text'] != "":
        messages.error(request, "Either select author from list or add new author. Cannot do both.")
        return redirect('/books/add')

    potential_authors = Author.objects.filter(full_name = request.POST['author_text'])

    if len(potential_authors) > 0:
        messages.error(request, "Author already exists! Please select from the list.")
        return redirect('/books/add')

    # FIX THIS
    # potential_books = Book.objects.filter(title = request.POST['title'], author = Author.objects.get(full_name = request.POST['full_name_select']))

    # if len(potential_books) > 0:
    #     messages.error(request, "Book already exists! Please add your review on existing book page.")
    #     return redirect('/books/add')
    if request.POST['author_select'] == "none" and request.POST['author_text'] != "":
        author_errors = Author.objects.basic_validator(request.POST)
        if len(author_errors) > 0:
            for key, val in author_errors.items():
                messages.error(request, val)
    book_errors = Book.objects.basic_validator(request.POST)
    review_errors = Review.objects.basic_validator(request.POST)

    if len(book_errors) > 0 or len(review_errors) > 0:
        for key, val in book_errors.items():
            messages.error(request, val)
        for key, val in review_errors.items():
            messages.error(request, val)
        return redirect('/books/add')

    if request.POST['author_select'] == "none" and request.POST['author_text'] != "":
        current_author = Author.objects.create(full_name = request.POST['author_text'])
    else:
        current_author = Author.objects.get(full_name = request.POST['author_select'])

    current_book = Book.objects.create(
        title = request.POST['title'],
        author = current_author,
    )
    current_book.reviewers.add(current_user)

    current_review = Review.objects.create(
        review = request.POST['review'],
        stars = request.POST['stars'],
        book = current_book,
        reviewer = current_user
    )
    
    return redirect(f'/books/{current_book.id}')

def single_book_page(request, book_id):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')

    current_user = User.objects.get(id=request.session['user_id'])

    current_book = Book.objects.get(id=book_id)

    context = {
        "user": current_user,
        "book": current_book,
        "reviews": current_book.reviews.all().order_by('-created_at')
    }

    return render(request, 'single_book.html', context)

def create_review(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')

    current_user = User.objects.get(id=request.session['user_id'])

    current_book = Book.objects.get(id=request.POST['book_id'])

    errors = Review.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect(f'/books/{ current_book.id }')


    Review.objects.create(
        review = request.POST['review'],
        stars = request.POST['stars'],
        reviewer = current_user,
        book = current_book
    )

    return redirect(f'/books/{ current_book.id }')

def delete_review(request, review_id):
    current_review = Review.objects.get(id = review_id)
    current_review.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def user_page(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')

    user = User.objects.get(id = user_id)
    review_count = user.reviews.count()
    user_reviewed_books = user.reviewed_books.all()

    context = {
        'user': user,
        'count': review_count,
        'books': user_reviewed_books
    }

    return render(request, 'user.html', context)

def logout(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in!")
        return redirect('/')

    request.session.clear()

    return redirect('/')

    