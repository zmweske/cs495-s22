from django import forms

class FlagForm(forms.Form):
    flag = forms.CharField(label='Flag', max_length=50, required=True)