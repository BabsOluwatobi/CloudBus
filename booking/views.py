

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import BusPass
from .forms import BusPassForm, EnhancedRegistrationForm # Added your new form here

def home(request):
    return render(request, 'booking/home.html')

def register_user(request):
    if request.method == 'POST':
        # Now using the enhanced form to capture email
        form = EnhancedRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = EnhancedRegistrationForm()
    return render(request, 'booking/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def logout_user(request):
    if request.method == 'POST': # Preferred for Django 5.0+
        logout(request)
        return redirect('home')
    # Fallback for GET requests if necessary
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    # Fixed the order_by to travel_date if booking_date doesn't exist in your model
    passes = BusPass.objects.filter(user=request.user).order_by('-travel_date')
    return render(request, 'booking/dashboard.html', {'passes': passes})

@login_required(login_url='login')
def book_pass(request):
    if request.method == 'POST':
        form = BusPassForm(request.POST)
        if form.is_valid():
            new_pass = form.save(commit=False)
            new_pass.user = request.user
            new_pass.save()
            return redirect('dashboard')
    else:
        form = BusPassForm()
    # Ensure this matches your template filename (book.html or book_pass.html)
    return render(request, 'booking/book.html', {'form': form})