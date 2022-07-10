from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registar_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First name must be more than 2 characters"
        if len(postData ['lname']) < 2:
            errors['lname'] = "Last name must be more than 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else:
            try:
                user = Users.objects.get(email__iexact=postData['email'])
            except:
                pass

        if postData['password'] != postData['confirm_password']:
            errors["passwords"] = "passwords are not matched!" 
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters" 
        return errors 


    def login_validator(self, postData):
        errors = {}
        EMAIL_REEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REEX.match(postData['email']):
            errors['email'] = "Email or password is wrong"
        else:
            try:
                user = Users.objects.get(email__iexact=postData['email'])
                if not bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
                    errors['login'] = "Email or password is wrong"
            except:
                errors['login'] = "Email or password is wrong"
        
        return errors



class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# class Posts(models.Model):
#     user = models.ForeignKey(Users, related_name='posts')