from django.shortcuts import render
from django.views import View
from api.form import CompanyForm, Feedback

# Create your views here.
def home_api(request):
    hello = "<h1> hellow how youar eyou </h1>"
    data = {
        'companyform' : CompanyForm, 
        'feedbackform' : Feedback,
        'hello' : hello,
    }
    return render(request, "index.html", data )


class cview(View):

    def get(self,request):
        print("INSIDE CLASS BASED VIEW HERE")
        a = request.GET.get('no')
        b = request.GET.get('name',"dkdkdkdk")
        c = request.GET.get('address')
        print(a,b,c)
        return render(request, "cview.html", {})


from rest_framework import viewsets
from api.models import Company
from api.serializers import company_Serializer

class companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = company_Serializer




