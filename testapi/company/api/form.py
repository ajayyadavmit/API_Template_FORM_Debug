from django import forms 

class Feedback(forms.Form):
    email = forms.CharField(label="enter email")
    detail = forms.CharField(label="Enter feedback details ")
    

# ———  creating FORMS through the mODEL Class —— 

from api.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['no','name','address']

