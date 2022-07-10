from django.db import models
import re
import datetime
from datetime import datetime, date

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data["first_name"]) < 2:
            errors["last_name"] = "First name should be at least 2 characters"
        if len(data["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(data["email"]):
            errors["email"] = "Email is invalid"
        if data["password"] != data["confirm_password"]:
            errors["password"] = "Passwords do not match"
        if len(data["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters in length"
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
    def validator(self, data):
        errors = {}
        if len(data["item"]) < 3:
            errors["item"] = "A wish must consist of at least 3 characters!"
        if len(data["description"]) < 3:
            errors["description"] = "A description of at least 3 characters must be provided!"
        return errors


class Wish(models.Model):
    item = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    granted = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="wish",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()


class Like(models.Model):
    liked = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name="likes",
                             on_delete=models.CASCADE)
    wish = models.ForeignKey(Wish, related_name="likes",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
