from django.shortcuts import render, redirect
from flower.form import Flower_Form_Model 
from django.views import View

from django.http import HttpResponse
from flower.models import FlowerDB

# Create your views here.
# FUnction based Views 
# def flower_home(request):
#     FormFLower = Flower_Form_Model()
#     data = {
#         'form' : FormFLower
#     }
#     return render(request, "flower_homePage.html", data)


# Class Based Views 

class Flower_home_class(View):
    # breakpoint()
    def get(self,request):
        print("Class based VIES POST MEthod here >>")
        FormFLower = Flower_Form_Model()
        f = FlowerDB.objects.all()

        data = {
            'form' : FormFLower,
            'f'  : f
        }
        return render(request, "flower_homePage.html", data)



def flower_order(request):

    if request.method == 'POST':
        n = request.POST.get('name')
        p = request.POST.get('price')
        no = request.POST.get('no')
        mobile_no = request.POST.get('mobileno')
        adds = request.POST.get('address')
        pic = request.POST.get('picture')
        print(n,p,no)
        print(type(p),type(no))
        print("Data Received Here ")
        tp = int(p) * int(no)
        print("Piecture revived Success", pic)

        form1 = Flower_Form_Model(request.POST, request.FILES)
        # breakpoint()
        if form1.is_valid():
            print("isnsie form valid")
            form1.save()
        else: 
            print("NO FORM Valid")
            print(form1.errors)
        data = {
            'name' : n,
            'totalprice' : tp, 
            'mobile_no' : mobile_no,
            'address' : adds

        }
        return render(request,"flower_order_confirmation.html",data)
    
    else: 
        return redirect('/flowerorder/')

def deleteFlower(request,value):
    # return HttpResponse("Delete order here ")
    print(value)
    f = FlowerDB.objects.all()
    f1 = FlowerDB.objects.get(id= value)
    f1.delete()
    data = {
        'f' : f
    }
    return render(request, "delete_flower_order.html", data)