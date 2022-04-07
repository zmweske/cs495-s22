from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Solution
from .forms import FlagForm

# import zach's code

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
    #do nothing, will use tokens to do zach's file patching
    return HttpResponseRedirect('/')