from statistics import multimode
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
            
            try:
                cursor = connection.cursor()
                sqlStatment = "SELECT username FROM login_patient WHERE username=\'"+username+"\' AND password=\'"+password+"\'"
                cursor.execute(sqlStatment)
                record = cursor.fetchone()    
            except:
                return render(request, 'login.html', {'error_message': 'ERROR- Check your MySQL Syntax before continuing'})
            if record == None:
                return render(request, 'login.html', {'error_message': 'Incorrect username or password!'})
            
            username = record[0]
            user = Patient.objects.get(username=username)
            return render(request, 'success.html', context={"user" : username, "date" : user.patient_since})
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