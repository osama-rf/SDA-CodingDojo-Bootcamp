from django.db import models
from datetime import datetime, timedelta

import re

# Create your models here.
# class UserManager(models.Manager):
#     def basic_validator(self, post_data):
#         errors = {}

#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z -]+$')
#         LAST_NAME_REGEX = re.compile(r'^[a-zA-Z -]+$')
#         MIN_AGE = 365*13
#         today = datetime.now()

#         if post_data['birthday'] != '':
#             birthday = datetime.strptime(post_data['birthday'], "%Y-%m-%d")


#         if len(post_data['first_name']) < 2:
#             errors['first_name'] = 'First name should have at least 2 characters.'
#         elif not FIRST_NAME_REGEX.match(post_data['first_name']):
#             errors['first_name'] = 'First name must consist of only letters'
        
#         if len(post_data['last_name']) < 2:
#             errors['last_name'] = 'Last name should have at least 2 characters.'
#         elif not LAST_NAME_REGEX.match(post_data['last_name']):
#             errors['last_name'] = 'Last name must consist of only letters and space or dash characters'

#         if len(post_data['alias']) < 1:
#             errors['alias'] = 'Alias required'
        
#         if post_data['birthday'] == '':
#             errors["birthday"] = "Please select a birthday"
#         elif birthday > today - timedelta(days=MIN_AGE):
#             errors["birthday"] = "You must be at least 13 years old to register"
#         elif birthday >= today:
#             errors["birthday"] = "Your birthday must be before today"
        
#         if len(post_data['email']) < 1:
#             errors['email'] = 'Email is required'
#         elif not EMAIL_REGEX.match(post_data['email']):
#             errors['email'] = 'Please enter a valid email address'
        
#         if len(post_data['password']) < 8:
#             errors['password'] = 'Password must be at least 8 characters'
#         if post_data['password'] != post_data['pw_confirm']:
#             errors['password'] = 'Passwords must match'

#         return errors

class User(models.Model):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    alias = models.CharField(max_length = 64)
    birthday = models.DateField(default = None)
    email = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # objects = UserManager()

class AuthorManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        FULL_NAME_REGEX = re.compile(r'^[a-zA-Z -.]+ +[a-zA-Z -.]+$')

        if len(post_data['author_text']) < 1:
            errors['full_name'] = "Author's full name is required"
        if not FULL_NAME_REGEX.match(post_data['author_text']):
            errors['full_name'] = "Author's full name should be first name and last name separated by a space."

        return errors

class Author(models.Model):
    full_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = AuthorManager()


class BookManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 1:
            errors['title'] = "Book Title is required"

        return errors

class Book(models.Model):
    title = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    author = models.ForeignKey(Author, related_name = 'books', on_delete = models.CASCADE)
    reviewers = models.ManyToManyField(User, related_name = 'reviewed_books')

    objects = BookManager()


class ReviewManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['review']) < 1:
            errors['review'] = "Review is required"
        if len(post_data['stars']) < 1:
            errors['stars'] = "Rating is required"

        return errors

class Review(models.Model):
    review = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    book = models.ForeignKey(Book, related_name = 'reviews', on_delete = models.CASCADE)
    reviewer = models.ForeignKey(User, related_name = 'reviews', on_delete = models.CASCADE)

    objects = ReviewManager()

