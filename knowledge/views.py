from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Solution
from .forms import FlagForm

import os
import time

# import zach's code
from .update import update_file

def knowledgeBase(request):
    solved = Solution.objects.filter(solved=True)
    if request.method == 'POST':
        form = FlagForm(request.POST)
        
        if form.is_valid():
            flag = form.cleaned_data['flag']
            
            try:
                solution = Solution.objects.get(flag=flag)
                solution.solved = True
                solution.save()
                solved = Solution.objects.filter(solved=True)
                return render(request, 'knowledgeBase.html', 
                    context = {'solution':solution, 'form':form, 'solved': solved})
            except:
                return render(request, 'knowledgeBase.html',
                    context = {'error_message': 'Flag not found', 'form': form, 'solved': solved})
                
    else:
        form = FlagForm()
        
    return render(request, 'knowledgeBase.html', {'form': form, 'solved': solved})
            
def patch(request, flag):
    solution = Solution.objects.get(flag=flag)
    tokens = solution.tokens
    mod_name = solution.mod_source
    name = solution.source
    file_path = mod_name+'/views.py'
    print(file_path)
    
    update_file(file_path, tokens["old_method"], tokens["new_method"])
    solution.fixed = True
    solution.save()
    #time.sleep(2000)
    return(knowledgeBase(request))
    
def revert(request, flag):
    solution = Solution.objects.get(flag=flag)
    tokens = solution.tokens
    mod_name = solution.mod_source
    name = solution.source
    file_path = mod_name+'/views.py'
    print(file_path)
    
    update_file(file_path, tokens["new_method"], tokens["old_method"])
    solution.fixed = False
    solution.save()
    
    return(knowledgeBase(request))