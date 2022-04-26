from django.shortcuts import render
from .forms import UploadFileForm
# Create your views here.


def handle_file(f):
    with open('upload/uploads/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.rsplit('.')[1] != 'pdf':
                return render(request, 'upload.html', {'form':form, 'error_message':"Not a pdf"})
            handle_file(file)
            return render(request, 'upload.html', {'form':form, 'context':"Success"})
        
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form':form})
