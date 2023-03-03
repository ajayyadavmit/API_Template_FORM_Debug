from django import forms
from passenger.models import PassengerDetails

class MarksCardPassenger(forms.Form):
    study = forms.CharField(label="Enter Passed Grade")
    mark = forms.IntegerField(label="Achived Marks out of 100")
    grade = forms.CharField(label="Grade achieved")
    comment = forms.Textarea()


class PassengerFormDB(forms.ModelForm):
    class Meta: 
        model = PassengerDetails
        fields = ['name','comments']




