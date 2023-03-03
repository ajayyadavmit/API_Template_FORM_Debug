from django import forms

from emp.models import Employee

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Enter email")
    name = forms.CharField(label="Enter your Name")
    feedback = forms.CharField(label="your feedback", widget=forms.Textarea)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','phone_no','location']

# with the meta class you can import the Model directly in the Form types... 
# model = Class Name 
# field ( Name of fields for the FORM )
# through django forms you can import forms directly to the code 