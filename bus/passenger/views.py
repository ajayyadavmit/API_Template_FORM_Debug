from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from passenger.models import PassengerDetails
from passenger.form import *

# Create your views here.
def pass_home(request):
    # return HttpResponse("Test Test Test Passenger")
    d1 = PassengerDetails.objects.all()
    f1 = MarksCardPassenger()
    f2 = PassengerFormDB()
    data = {
        'd1' : d1,
        'form' : f1,
        'f2' : f2
    }

    if request.method == 'GET':
        print("GET GET Request TYPES HERE >>> ")
        # v1 = request.GET.get('name1','dummy')
        # v2 = request.GET.get('name2','dummy')
        # v3 = request.GET.get('caste2','dummy')
        # v4 = request.GET.get('comments2','dummy')
        # v5 = request.GET.get('child_no2',4)

        f5= request.GET.get('name',"000")
        f6 = request.GET.get('comments',"8888")

        # print(v1, v2, v3,v4,v5)
        p = PassengerDetails()
        # p.name = v2
        # p.caste = v3
        # p.comments = v4
        # p.child_no = v5 

        p.name = f5
        p.comments = f6 

        p.save()

    return render(request, "pass.html", data)

def formsubmit(request):
    if request.method == 'POST':
        print("OPOST POST DATA HERE")
        s = request.POST.get('study')
        m = request.POST.get('mark')
        print(s,m)
        d1 = PassengerDetails()
        d1.name = s 
        d1.caste = m 
        d1.save()
    return HttpResponse("Thanks for SUCCESSFULLY SUBMITTING the FORM ")


def deletevalue(request, id_value):
    print(id_value)
    d1 = PassengerDetails.objects.get(pk= id_value)
    print(d1.__dict__)
    d1.delete()
    print("SUCSS Delete")
    return redirect('/pass/')



def updatedata(request, id_value):
    print("updating data here >>", id_value)
    u1 = PassengerDetails.objects.get(id = id_value)
    print(u1.name, u1.caste)
    data = {'u1' : u1 
            }

    return render(request, "update.html", data)


def deletepassenger(request,value):
    p = PassengerDetails.objects.get(id= value)
    print(p.__dict__)

    print(value)
    return HttpResponse(value)