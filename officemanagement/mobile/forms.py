from django import forms 

class Feedback(forms.Form):
    email = forms.CharField(label="enter email")
    detail = forms.CharField(label="ENter feedback details ")
    


