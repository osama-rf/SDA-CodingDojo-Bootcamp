from django.db import models
import re
import bcrypt
import datetime

class UserManager(models.Manager):
    def register_validation(self,postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First Name must be more than 2 characters "

        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name must be more than 2 characters "

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else:
            try:
                user = User.objects.get(email__iexact=postData['email'])
                errors['email'] = "Email is already registered try to login!"  
            except:
                pass
        
        birthday = datetime.datetime.strptime(postData['birthday'],"%Y-%m-%d") # convert the string date into datetime type
        bdHigherThan14 = datetime.datetime.today() - birthday # substract today date from the birthday given a timedelta type
        if len(postData['birthday']) == 0:
            errors['birthday'] = "Date of Birth is reqiured"
        elif birthday > datetime.datetime.today():
            errors['birthday'] = "Date of Birth should be in the past !"
        elif bdHigherThan14.days < 365 * 13: # compare number of days in the DoB with 13years days .
            errors['birthday'] = "Minimum age requirment is 13 age try next years :) "

        if postData['password'] != postData['confirm_password']:
            errors["passwords"] = "passwords are not matched!" 

        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters" 
        
        return errors

    def login_validation(self,postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else:
            try:
                user = User.objects.get(email__iexact=postData['email'])
                if not bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
                    errors['login'] = "Email or Password is incorrect !"
            except:
                errors['login'] = "Email or Password is incorrect !"
        
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(default="1999-01-01")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def book_validator(self,postData):
        errors = {}
        if len(postData['title'])<1:
            errors['title']="You must include the title."
        if len(postData['description'])<5:
            errors['description']="Your description must be at least 5 characters."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User,related_name="book_uploader",on_delete=models.CASCADE)
    users_who_like =models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()