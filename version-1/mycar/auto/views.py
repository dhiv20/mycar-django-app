
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def cars(request):
    return render(request, 'cars.html')

def contact(request):
    return render(request, 'contact.html')





# Create your views here.
