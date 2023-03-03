from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):
    # return HttpResponse(" TEst INDEX Web Page")
    print(request.method)
    print("GETTING DTATAS HERE ")

    if request.method == 'GET':
        a = request.GET.get('name1')
        print(a)
    if request.method == 'POST':
        a = request.POST['name1']
        a1 = request.POST.get('name1')
        r1 = request.POST.get('radio1')
        c1 = request.POST.get('check')
        print("POST POST DATA HERE")
        print(a,a1, r1, c1)

    date = datetime.datetime.now()
    isActive = True
    name = "ajay yadav "
    program_list = [
        'one', "two","theree"
    ]
    student = {
        'name' : "rahul",
        'college' : "MIT",
        'city' : "kathmandu",
    }
    data = {
        'isActive' : isActive,
        'name' : name , 
        'date' : date ,
        'program_list' : program_list, 
        'student_data' : student,

    }
    return render(request, "home.html", data)



def about(request):
    # return HttpResponse(" ABOUT ABOUT PAGE ")
    return render(request, "about.html",{})

def services(request):
    # return HttpResponse("SERVICES SERVICES ")
    return render(request, "services.html", {})

# include tage in the html pages ... with the templates.. there... 
# data can be send from Templates to VIEWS through request parameter and from view to templates through dictionary functional arguments types... 
