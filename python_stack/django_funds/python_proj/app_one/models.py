from django.db import models
import re
import bcrypt
from datetime import datetime, timedelta
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if len(post_data['fname']) < 2:
            errors['fname'] = "First name must be at least 2 characters"
        if len(post_data['lname']) < 2:
            errors['lname'] = "Last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email format"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characterse"
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Passwords do not match"
        print("reached the validator for register")
        user_list = User.objects.filter(email=post_data['email'])
        if len(user_list) > 0:
            errors['not_unique'] = "Email already exists"
        return errors

    def login_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email format"

        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        user_list = User.objects.filter(email=post_data['email'])
        if len(user_list) == 0:
            errors['email2'] = "Email does not exist"
        elif not bcrypt.checkpw(post_data['password'].encode(), user_list[0].password.encode()):
            errors['match'] = "Password does not match the db"
        return errors


class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class WishManager(models.Manager):
    def wish_validator(self, postData):
        errors = {}
        if len(postData['theWish']) < 3:
            errors['theWish'] = "Item must be at least 3 characters."
        if len(postData['desc']) < 3:
            errors['desc'] = "Description must at least 3 characters."
        return errors

class Wish(models.Model):
    theWish = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="wishes", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = WishManager()

class Wish_granted(models.Model):
    theWish = models.CharField(max_length=255)
    # likes = models.ManyToManyField(User, related_name='likes')
    user = models.ForeignKey(User, related_name="wishes_granted", on_delete = models.CASCADE)
    added_date = models.DateTimeField(auto_now=True)
    granted_date = models.DateTimeField(auto_now_add=True)
    