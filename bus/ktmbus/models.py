from django.db import models

# Create your models here.

class BusDB(models.Model):
    name = models.CharField(max_length=11)
    amount = models.IntegerField()
    location = models.CharField(max_length=11, default="ABC")
    city = models.CharField(max_length=11, default="KTM")

    def __str__(self):
        return self.name


