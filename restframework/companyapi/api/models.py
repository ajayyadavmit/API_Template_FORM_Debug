from django.db import models

# Create your models here.
# Create Company Models 


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=11)
    location = models.CharField(max_length=45)
    comment = models.TextField()


#Create a SERIALIZERS  to make the DATA CONVERt from MODEL DB to the JSON FORMATS DB to JSON FORMATS.... 


