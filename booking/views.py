from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import BusPass
from .forms import BusPassForm

def home(request):
    return render(request, 'booking/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
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
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    passes = BusPass.objects.filter(user=request.user).order_by('-booking_date')
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
    return render(request, 'booking/book.html', {'form': form})