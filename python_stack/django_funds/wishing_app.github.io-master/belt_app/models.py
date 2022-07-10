from django.db import models
import re
from datetime import datetime, date
import bcrypt



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):                
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] ='Password should be at least 8 characters'
        if postData['password'] != postData['conf_password']:
            errors['conf_password'] = 'Passwords should match'         
        result = User.objects.filter(email=postData['email'])
        if len(result) > 0:
            errors['email'] = 'Email has already been registered!'
            
        return errors
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class WishManager(models.Manager):
    def wish_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 3:
            errors["title"] = "A wish should be at least 3 characters"
        if postData['desc'] == "":
            errors["desc"] = "Description must be provided"
            
        return errors   
    
class Wish(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.CharField(max_length=255)
    poster=models.ForeignKey(User, related_name = "has_wishes", on_delete=models.CASCADE)
    grant_wish = models.BooleanField(default=0)
    grant_created = models.DateTimeField(null=True, blank= True)
    liked_by = models.ManyToManyField(User, related_name='liked_wishes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()
    
    

    

