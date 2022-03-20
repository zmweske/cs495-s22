from django.shortcuts import render

from .models import Doctor

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            #Make list of form input based on space separation
            name=form.cleaned_data['name'].rsplit(' ')
            
            #Will search for either name in db if space exists
            first_name = name[0]
            last_name = '' if len(name) < 2 else name[1]
            
            Doctor.objects.filter(first_name)
            