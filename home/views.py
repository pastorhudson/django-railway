from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from .forms import SignupForm  # Adjust the import path according to your project structure


def index(request):
    return TemplateResponse(request, 'home/home.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a new URL
    else:
        form = SignupForm()
    return render(request, 'home/signup.html', {'form': form})
