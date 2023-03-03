from django.shortcuts import render, redirect
from django.http import HttpResponse
from emp.models import Employee, Testimonal
from emp.forms import FeedbackForm, EmployeeForm

# Create your views here.
def emp_home(request):
    # return HttpResponse("student HOME PAGE ")
    emp = Employee.objects.all()
    return render(request, "emp/home.html", {'emp': emp})

'''
def emp_home(request): function 
emp = Employee.objects.all() # retrives all the value of objects.. 
return render(request, "emp/home.html", {} Dictionary values.. {'emp': emp}) NOw you can use this dictionary values in the TEMPLATES Functions... 

request.method == 'POST':
request.POST.get('name1')
request.POST.get('name22')  # this gives the Tag values of the objects.. 

creation of the MOdel constructore first... with the class nmaes... 
std = Student() Constructores 
std.name = n ( from request values )
std.cousre = c ( from request values. )
'''

def add_emp(request):
    if request.method == 'POST':
        print("Data is coming to add EMP Page")
        # data fetch 
        n = request.POST.get("name")
        p = request.POST.get("phone")
        l = request.POST.get("loc")
        print(n,p,l)

        # save model to the datbases through queries.. 
        #creation of Object for the DB and fetiching the details through object queries..add()
        e = Employee()
        e.name = n
        e.phone_no = p
        e.location = l
        e.save()
        return redirect('/emp/home/')
    form = EmployeeForm()
    return render(request, "emp/add_emp.html", {'form': form})

# This is delete funtion of the employee and data is rendered to the view to the Templates... 

def delete_emp(request, emp_id):
    print(emp_id)
    print("#"*33)
    e= Employee.objects.get(pk=emp_id)
    e.delete()
    print("DELETED EMPLOYEE DEtails here >>> ")
    # return HttpResponse(emp_id)
    return redirect('/emp/home/')
#e.delete() for the deleting the data's....  e object is there to delete() funcs values.. 

def update_emp(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    return render(request, "emp/update_emp.html", {'emp' : emp})

    # return redirect('/emp/home/')

def emp_testimonals(request):
    # return HttpResponse("EMPloyee TESTIMONALS TESTIMONALS HERE >>> ")
    testi = Testimonal.objects.all()
    return render(request, "emp/testimonals.html", {'testi' : testi})

#meanin of slash in the render and redirect functions.. // makes doees not work out.. 

def emp_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            form.cleaned_data['feedback']


        else:
            return render(request, "emp/feedback.html",{'form' : form})

    else: 
        form = FeedbackForm()
        return render(request, "emp/feedback.html",{'form' : form})

