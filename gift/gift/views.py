from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect


def gifthome(request):
    # return HttpResponse("GIFT HOME PAGE HERE ")
    return render(request, "gift.html", {})

def starter(request):
    return render(request, "starter.html", {})


def extend(request):
    return render(request, "extend1.html", {})
