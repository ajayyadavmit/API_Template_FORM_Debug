from django.shortcuts import render

# Create your views here.

def emphome(request):
    return render(request,"emphome.html",{})