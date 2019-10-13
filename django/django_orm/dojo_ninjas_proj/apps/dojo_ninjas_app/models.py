from django.db import models


class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    desc = models.TextField()

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojo, related_name='ninjas')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)


