from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    a,b,c = 1,2,3
    d,e,f = 4500, 350044.2, 8494949494.748484
    l = [a,b,c]
    l2 = [d,e,f]
    v= "this is good one"
    hello = "<h1> index page </h1>"
    data = {
        'l' : l,
        'l2' : l2,
        'v' : v,
        "hello" : hello,


    }
    return render(request, "index.html", data)

