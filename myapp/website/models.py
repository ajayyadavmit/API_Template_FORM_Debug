from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=22)
    college = models.CharField(max_length=22)
    age = models.IntegerField(max_length=10)

    