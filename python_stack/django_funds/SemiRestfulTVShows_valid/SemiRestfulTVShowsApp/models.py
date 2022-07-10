from django.db import models

# Assignment Check list
# 1- Validate the Add a TV Show form to ensure all fields are populated appropriately before adding to the database.

class validCheck(models.Manager):
    def showValidator(request, data):
        errors = {}

        if len(data['title']) < 2:
            errors['title'] = "The title should be more than 2 string"
        if len(data['network']) < 3:
            errors['network'] = "The network name should be more than 3 string"
        if len(data['description']) < 10:
            errors['description'] = "The length of description should be more than 10 characters"
        return errors

    def updateValidator(request, data):
        errors = {}

        if len(data['title']) < 2:
            errors['title'] = "The title should be more than 2 string"
        if len(data['network']) < 3:
            errors['network'] = "The network name should be more than 3 string"
        if len(data['description']) < 10:
            errors['description'] = "The length of description should be more than 10 characters"
        return errors





class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= validCheck()



