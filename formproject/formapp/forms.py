from django import forms

class Myforms(forms.Form):
    name=forms.CharField(max_length=20)
    address=forms.CharField(max_length=50)
    age=forms.IntegerField()
    phoneNo=forms.RegexField(regex=r"^\d{10}$")