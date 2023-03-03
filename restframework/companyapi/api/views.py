from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import Company
from api.serializers import company_Serializer

class companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = company_Serializer


# First rest framwork added, then DB model created  then >> Serializers created for converting the DATAs >> then view set is added to make the URL call >> then URL py file crated 

