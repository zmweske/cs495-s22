from django.shortcuts import render
from django.db.models import Q

from .models import Doctor
from .forms import SearchForm

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            #Make list of form input based on space separation
            #name=form.cleaned_data['name'].rsplit(' ')
            
            #Will search for either name in db if space exists
            #first_name = name[0]
            #last_name = name[0] if len(name) < 2 else name[1]
            
            match_queryset = Doctor.objects.filter(first_name__contains=form.cleaned_data['name'])
            #match_queryset = Doctor.objects.filter(Q(first_name__icontains=first_name) | Q(first_name__icontains=last_name) | Q(last_name__icontains=first_name) | Q(last_name__icontains=last_name))
            queryset = match_queryset.filter(hidden=False)
            
            return render(request, 'search.html', context={'queryset':queryset, 'form': form})  
            
        
    else:
        form = SearchForm()
        
    return render(request, 'search.html', {'form': form})
