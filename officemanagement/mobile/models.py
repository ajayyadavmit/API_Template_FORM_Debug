from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=11)
    cost = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    