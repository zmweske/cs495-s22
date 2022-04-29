from django.shortcuts import render

from .forms import PaymentForm

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['cost'] > 0:
                return render(request, 'payment.html', {'form':form, 'error_message':"Not enough funds"})
            return render(request, 'payment.html', {'form':form, 'success':"success"})
        return render(request, 'payment.html', {'form':form, 'error_message':"Not enough funds"})
        
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form':form})
