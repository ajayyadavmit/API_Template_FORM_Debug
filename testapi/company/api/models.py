from django.db import models

# Create your models here.
class Company(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=22)
    address = models.TextField()
    location = models.CharField(max_length=22)


    