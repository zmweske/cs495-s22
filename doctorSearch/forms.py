from django import forms
from .models import Doctor

class SearchForm(forms.Form):
    name = forms.CharField(label='Name', max_length=60, required=True)