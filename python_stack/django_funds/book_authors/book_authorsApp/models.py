from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Book,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
