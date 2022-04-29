from django import forms

class PaymentForm(forms.Form):
    CHOICES = (('Stethoscope', 'Stethoscope'),('Scrubs','Scrubs'),('Parking Pass', 'Parking Pass'))
    item = forms.ChoiceField(choices=CHOICES)
    cost = forms.IntegerField(initial=100, required=True)