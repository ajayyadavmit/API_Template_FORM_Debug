from django.shortcuts import render

# Create your views here.

from app.models import Student

def index(request):
    obj = Student.objects.all()
    return render(request, "index.html", {"obj" : obj})

