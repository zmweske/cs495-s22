from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.db import connection

from .forms import LoginForm
from .models import Patient

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            
            cursor = connection.cursor()
            cursor.execute("SELECT username FROM login_patient WHERE username=\'"+username+"\' AND password=\'"+password+"\'")
            record = cursor.fetchone()    
            
            if record == None:
                return render(request, 'failure.html')
            
            user = record[0]
            return render(request, 'success.html', context={"user" : record[0]})
            # user = Patient.objects.get(username=form.cleaned_data['username'])
            
            # if user.password == form.cleaned_data['password']:
            #     return render(request, 'success.html')
            #     #return HttpResponseRedirect('/success/')
            
            # else:
            #     return render(request, 'failure.html')
            #     #return HttpResponseRedirect('/failure/')
            
        
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def failure(request):
    return render(request, 'failure.html')