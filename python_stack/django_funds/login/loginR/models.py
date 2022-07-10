from django.db import models

class userManager(models.Manager):
    def validator(self, postData):
        errors = {}
        return errors

class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    creeated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = userManager()











