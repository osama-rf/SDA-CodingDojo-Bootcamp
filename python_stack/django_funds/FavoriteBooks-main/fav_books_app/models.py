from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid Email/Password!"

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"

        if (postData['password']!= postData['confirm_password']):
            errors['confirm_password'] = "Confirm password did not match"

        # user = User.objects.filter(email=postData['email'])
        # if(len(user)> 0):
        #     errors['email_password'] = 'Email/Password is correct.'
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])

        if len(user)== 0:
            errors['email_password'] = "Email/password is incorrect."

        else:
            if bcrypt.checkpw(
                postData['password']. encode(), user[0].password.encode()
            )!= True:
                errors['email_password'] = "Email/Password is incorrect"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    #books_uploaded (one-to-many - a list of books uploaded by a given user)
    #liked_books (many-to-many - a list of books a given user likes)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors["title"] = "Title is required"
        if len(postData['description']) < 5:
            errors["description"] = "Description must be at least 2 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=800)
    uploaded_by = models.ForeignKey(User, related_name = 'books_uploaded', on_delete = models.CASCADE)
        #one-to-many: THE user who uploaded a GIVEN book
    users_who_like = models.ManyToManyField(User, related_name = 'liked_books')
        #many-to-many: a LIST of USERS who like a GIVEN book
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
