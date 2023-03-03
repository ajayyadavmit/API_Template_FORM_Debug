from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=22)
    phone_no = models.IntegerField()
    location = models.CharField(max_length=22)

    def __str__(self) -> str:
        return self.name
    
class Testimonal(models.Model):
    name = models.CharField(max_length=22)
    feedback = models.TextField()
    picture = models.ImageField(upload_to="testimonals/")

    def __str__(self):
        return self.feedback
