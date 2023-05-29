from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def read(request):
    return render(request, 'read.html')

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')
