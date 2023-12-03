# forms.py
from django import forms

class OpinionForm(forms.Form):
    name = forms.CharField(max_length=100)
    cruise = forms.CharField(max_length=100)
    opinion = forms.CharField(widget=forms.Textarea)
