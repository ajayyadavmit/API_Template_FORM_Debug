from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=11)
    marks = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)
    adds = models.TextField()
    # age = models.IntegerField(default=11)

    def __str__(self):
        return self.name
    

class newstudent(Student):
    isbn = models.TextField()


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
