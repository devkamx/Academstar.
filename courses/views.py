from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'courses/index.html')

def courses(request):
    return render(request, 'pages/contact.html')

def search(request):
    return render(request, 'pages/contact.html')

