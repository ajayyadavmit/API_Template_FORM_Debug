from django.db import models

# Create your models here.
from django.db import models 

class PassengerDetails(models.Model):
    name = models.CharField(max_length=11, default="NEW")
    caste = models.CharField(max_length=11, default="Caste ABC")
    comments = models.TextField(default="abc comments")
    child_no = models.IntegerField(default=2)


    def __str__(self):
        return self.name 
    
class xyz(models.Model):
    name = models.CharField(max_length=11)
    caste = models.CharField(max_length=11)
    comments = models.TextField()
