from django.shortcuts import render
from django.db.models import Q
from django.db import connection

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
            
            #match_queryset = Doctor.objects.filter(first_name__contains=form.cleaned_data['name'])
            #match_queryset = Doctor.objects.filter(Q(first_name__icontains=first_name) | Q(first_name__icontains=last_name) | Q(last_name__icontains=first_name) | Q(last_name__icontains=last_name))
            #queryset = match_queryset.filter(hidden=False)
            
            #return render(request, 'search.html', context={'queryset':queryset, 'form': form}) 
            errorMsg = None
            records = None 
            name = form.cleaned_data['name'].rsplit(' ')
            if(len(name) > 1):
                firstName = name[0]
                lastName = name[1]
            else:
                firstName = name[0]
                lastName = name[0]

            try:
                cursor = connection.cursor()
                sqlStatement = "SELECT id, first_name, last_name, department FROM doctorSearch_doctor WHERE first_name=\'"+firstName+"\' OR first_name=\'"+lastName+"\' OR last_name=\'"+firstName+"\' OR last_name=\'"+lastName+"\'"
                cursor.execute(sqlStatement)
                records = cursor.fetchall()

            except:
                #return render(request, 'login.html', {'error_message': 'ERROR- Check your MySQL Syntax before continuing', 'form': form})
                errorMsg = 'ERROR- Check your MySQL Syntax before continuing'
                
            if records == None and errorMsg == None:
                #return render(request, 'login.html', {'error_message': 'Incorrect username or password!', 'form': form})
                errorMsg = 'Incorrect username or password!'

            if errorMsg == None:
                doctorInfo = []
                for record in records:
                    info = {"firstName": record[1], "lastName": record[2], "department": record[3]}
                    doctorInfo.append(info)

                return render(request, 'search.html', context={'queryset': doctorInfo, 'form': form})
            
            return render(request, 'search.html', {'error_message': errorMsg, 'form': form})

            
        
    else:
        form = SearchForm()
        
    return render(request, 'search.html', {'form': form})
