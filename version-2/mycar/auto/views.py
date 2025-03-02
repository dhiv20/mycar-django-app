
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def cars(request):
    return render(request, 'cars.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a 'thank you' page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')

# Create your views here.
