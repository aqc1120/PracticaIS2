from django import forms
from .models import Cruise

class OpinionForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cruise = forms.ModelChoiceField(queryset=Cruise.objects.all(), label='Crucero', widget=forms.Select(attrs={'class': 'form-control'}))
    opinion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Opinión')
