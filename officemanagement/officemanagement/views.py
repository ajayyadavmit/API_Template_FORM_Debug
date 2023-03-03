from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect

from mobile.models import Phone

def home(request):
    if request.method == 'GET':
        print("Getting GET request here >>> ")
        email = request.GET.get('email_data')
        txt = request.GET.get('text_name')
        print(email, txt, "    ######  ")
        email1 = request.GET.get('email_data1')
        txt1 = request.GET.get('text_name1')
        print(email1, txt1)
    return render(request, "home.html", {})

def index(request):
    print("Index INdex URL Here ")
    if request.method == 'GET':
        v1 = request.GET.get('t2')
        c1 = request.GET.get('cost')
        print("#"*22)
        print(v1,c1)

        p = Phone()
        p.name = v1
        p.cost = c1
        p.save()
    dataPhone = Phone.objects.all()

    return render(request, "index.html", {'data' :dataPhone})

def deletePhone(request,dph):
    p2 = Phone.objects.get(id=dph)
    p2.delete()
    print("Deleteed the phone objects")
    return redirect('/home-home/')
    # return HttpResponseRedirect('/home-home/')


#httpresponseredirect('url path here' )  >> url path here ... 

