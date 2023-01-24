from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def index(request):
    return HttpResponse("It's working")

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('')
    else:
        form = UserRegistrationForm()
    return redirect('')
