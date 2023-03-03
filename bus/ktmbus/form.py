from django import forms 
from ktmbus.models import BusDB

class feedback(forms.Form):
    email = forms.EmailField(label="EMail")
    name = forms.CharField(label="Name")


class BusForm(forms.ModelForm):
    class Meta:
        model = BusDB
        fields = ['name','amount','location']

 