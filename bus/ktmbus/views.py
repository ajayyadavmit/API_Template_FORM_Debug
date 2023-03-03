from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from ktmbus.models import BusDB 


def busview(request):
    return HttpResponse("BUS INSIDE VIEW Data's")


def localbus(request):
    b = BusDB()
    if request.method == 'GET':
        name = request.GET.get('name1')
        amount = request.GET.get('amount')
        print(type(name))
        print(name,amount)
        if name : 
            b.name = name
            b.amount = amount
            b.save()
            return redirect(localbus)
        else:
            print("Data is not sufficient {name}  and {amount}")
    

    print("LOCAL BUS DATA ")
    return render(request, "localbus.html", {})
from ktmbus.form import *

def mainbus(request):
    data1 = BusDB.objects.all()
    l = [45,34,23]
    n = "ajay"
    form = feedback()
    c = {'course' :"english",
         "marks" : [34,23,55]}
    f1 = BusForm()
    
    data = {'data1' : data1,
            'l' : l, 
            'n' : n ,
            'c' : c ,
            'form' : form ,
            'f1' : f1}

    print("INside MAIN BUS data ")

    return render(request, "mainbus.html", data)


