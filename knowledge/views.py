from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Solution
from .forms import FlagForm

import os

# import zach's code
from .update import update_file

def knowledgeBase(request):
    if request.method == 'POST':
        form = FlagForm(request.POST)
        
        if form.is_valid():
            flag = form.cleaned_data['flag']
            
            try:
                solution = Solution.objects.get(flag=flag)
                return render(request, 'knowledgeBase.html', 
                    context = {'solution':solution, 'form':form})
            except:
                return render(request, 'knowledgeBase.html',
                    context = {'error_message': 'Flag not found', 'form': form})
                
    else:
        form = FlagForm()
        
    return render(request, 'knowledgeBase.html', {'form': form})
            
def patch(request, flag):
    solution = Solution.objects.get(flag=flag)
    tokens = solution.tokens
    mod_name = solution.mod_source
    name = solution.source
    file_path = mod_name+'/views.py'
    print(file_path)
    
    update_file(file_path, tokens["old_method"], tokens["new_method"])
    
    return HttpResponseRedirect('/'+name+'/')
    
    