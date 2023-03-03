from django.http import HttpResponse

from django.shortcuts import render, redirect


def home_page(request):
    return render(request,"homepage.html", {})

def wel(request):
    return render(request,"welcome.html", {})