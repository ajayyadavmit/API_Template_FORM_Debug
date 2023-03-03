from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home_page(request):
    name = ["ram","shayd","hari"]
    # return HttpResponse("THis is home page ")
    return JsonResponse(name, safe=False)