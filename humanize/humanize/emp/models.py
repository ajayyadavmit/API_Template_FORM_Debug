from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=11)
    age = models.IntegerField()
    adds = models.CharField(max_length=11)

    