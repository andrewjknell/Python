from django.db import models
import re, bcrypt
from datetime import date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        if len(postData['first']) < 2:
            errors['first'] = 'name must be at least 2 characters long'    
        if len(postData["last"]) < 2:
            errors["last"] = 'name must be at least 2 characters long'
        if User.objects.filter(email = postData['email']):
            errors['email_taken'] = "This email is already being used"
        if EMAIL_REGEX.match(postData['email']) == None:
            errors['email_format'] = "must be a valid email"
        if len(postData['password']) < 8:
            errors['password_len'] = "password must have at least 8 characters"
        if postData['password'] != postData['checkpw']:
            errors['checkpw'] = "passwords must match"
        return errors


    def loginValidator(self, postData):
        user = User.objects.filter(email = postData['login_email'])
    
        errors = {}
        if not user:
            errors['email'] = "enter a valid email"
        if user and not bcrypt.checkpw(postData['login_password'].encode('utf8'), user[0].password.encode('utf8')):
            errors['password'] = "invalid password"
        return errors


    def newBookValidator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = 'must have a title'
        if len(postData['desc']) < 5:
            errors['desc'] = 'description must be longer than 5 characters'
        return errors

        
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = userManager()
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = userManager()