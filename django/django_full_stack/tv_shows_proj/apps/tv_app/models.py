from django.db import models



class ShowManager(models.Manager):
    def basic_validation(self, postData):
        errors ={}
        if len(postData['title']) < 2:
            errors['title'] = 'show name must be at least 2 characters long'    
        if len(postData["network"]) < 2:
            errors["network"] = 'network name must be at least 2 characters long'
        if len(postData["desc"]):
            if len(postData["desc"]) < 10:
                errors["desc"] = "description must be more than 10 characters"
    
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


