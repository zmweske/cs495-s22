from django.shortcuts import render
from django.db.models import Q
from django.db import connection

from .models import Doctor
from .forms import SearchForm

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            errorMsg = None
            records = None 
            name = form.cleaned_data['name'].rsplit(' ')
            
            #Will search for either name in db if space exists
            # first_name = name[0] # method_1
            # last_name = name[0] if len(name) < 2 else name[1] # method_1
            
            # #match_queryset = Doctor.objects.filter(first_name__contains=form.cleaned_data['name']) # method_1
            match_queryset = Doctor.objects.filter(Q(first_name__icontains=first_name) | Q(first_name__icontains=last_name) | Q(last_name__icontains=first_name) | Q(last_name__icontains=last_name))
            # queryset = match_queryset.filter(hidden=False) # method_1
            
            # return render(request, 'search.html', context={'queryset':queryset, 'form': form}) # method_1 
            
            if(len(name) > 1): # method_2
                first_name = name[0] # method_2
                last_name = name[1] # method_2
            else: # method_2
                first_name = name[0] # method_2
                last_name = name[0] # method_2

            try: # method_2
                cursor = connection.cursor() # method_2
                sqlStatement = "SELECT id, first_name, last_name, department FROM doctorSearch_doctor WHERE first_name=\'"+first_name+"\' OR first_name=\'"+last_name+"\' OR last_name=\'"+first_name+"\' OR last_name=\'"+last_name+"\'" # method_2
                cursor.execute(sqlStatement) # method_2
                records = cursor.fetchall() # method_2

            except: # method_2
                errorMsg = 'ERROR- Check your MySQL Syntax before continuing' # method_2
                
            if records == None and errorMsg == None: # method_2
                errorMsg = 'Incorrect username or password!' # method_2

            if errorMsg == None: # method_2
                doctorInfo = [] # method_2
                for record in records: # method_2
                    info = {"firstName": record[1], "lastName": record[2], "department": record[3]} # method_2
                    doctorInfo.append(info) # method_2

                return render(request, 'search.html', context={'queryset': doctorInfo, 'form': form}) # method_2
            
            return render(request, 'search.html', {'error_message': errorMsg, 'form': form}) # method_2

            
        
    else:
        form = SearchForm()
        
    return render(request, 'search.html', {'form': form})
