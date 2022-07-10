from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        user = User.objects.filter(email = postData['email'])
        if (user[0].email != postData['email']):
            errors['email'] = "error has accured"
        user = User.objects.filter(email = postData['email'])
        if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            errors['password'] = "error has accured"
        return errors

    def registration_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        elif len(postData['password']) < 8:
            errors['password'] = "password should be at least 8 characters"
        elif (postData['password'] != postData['cPassword']):
            errors['cPassword'] = "password is not equal to the confirm password"
        elif len(postData['name']) < 2:
            errors['name'] = "name should be at least 2 characrters long"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    pic = models.TextField()
    liked_by = models.ManyToManyField(User, related_name="likes")
    users_list = models.ManyToManyField(User, related_name="lists")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
