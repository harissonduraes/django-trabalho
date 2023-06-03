from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'usuarios/index.html', {})

def w3c(request):
    return render(request, 'usuarios/w3c.html')

def html(request):
    return render(request, 'usuarios/html.html')