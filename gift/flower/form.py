from django import forms

from flower.models import FlowerDB

class Flower_Form_Model(forms.ModelForm):
    class Meta:
        model = FlowerDB
        fields = ['name','price','no', 'mobileno', 'address','picture']

