from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    age = models.IntegerField()
