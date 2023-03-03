from django.db import models

# Create your models here.
class FlowerDB(models.Model):
    name = models.CharField(max_length=11)
    price = models.IntegerField()
    no = models.IntegerField()
    total_price =  models.IntegerField(default=11)
    mobileno = models.IntegerField()
    address = models.CharField(max_length=11)
    picture = models.ImageField(upload_to='pictures/')
    