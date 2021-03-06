from statistics import multimode
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.db import connection

from .forms import LoginForm
from .models import Patient

def login(request):
    errorMsg = None
    record = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            try: # method_1
                cursor = connection.cursor() # method_1
                sqlStatment = "SELECT username FROM login_patient WHERE username=\'"+username+"\' AND password=\'"+password+"\'" # method_1
                cursor.execute(sqlStatment) # method_1
                record = cursor.fetchone()    # method_1
            except: # method_1
                return render(request, 'login.html', {'error_message': 'ERROR- Check your MySQL Syntax before continuing', 'form': form}) # method_1
            if record == None: # method_1
                return render(request, 'login.html', {'error_message': 'Incorrect username or password!', 'form': form}) # method_1
            
            username = record[0] # method_1
            
            # try: # method_2
                # user = Patient.objects.get(username=username) # method_2
                # if Patient.objects.get(username=username).password == password: # method_2
                    # return render(request, 'success.html', context={"user" : username, "date" : user.patient_since}) # method_2
                # else: # method_2
                    # return render(request, 'login.html', {'error_message': 'Incorrect username or password!', 'form': form}) # method_2

            # except: # method_2
                # return render(request, 'login.html', {'error_message': 'Incorrect username or password!', 'form': form}) # method_2

            user = Patient.objects.get(username=username)
            return render(request, 'success.html', context={"user" : username, "date" : user.patient_since}) # method_1                             
                        
            
        
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form, 'navbar': 'login'}) # method_htmlU
    # return render(request, 'login_noleak.html', {'form': form, 'navbar': 'login'}) # method_htmlS

def home(request):
    return render(request, 'home.html', {'navbar': 'home'})

def success(request):
    return render(request, 'success.html')

def failure(request):
    return render(request, 'failure.html')