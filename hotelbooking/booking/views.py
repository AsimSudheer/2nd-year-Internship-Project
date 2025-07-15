from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Hotel, Booking
from .forms import BookingForm

def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'booking/home.html', {'hotels': hotels})

def about(request):
    return render(request, 'booking/about.html')

def contact(request):
    return render(request, 'booking/contact.html')

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/dashboard.html', {'bookings': bookings})

@login_required
def book_hotel(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking successful!")
            return redirect('dashboard')
    else:
        form = BookingForm()
    return render(request, 'booking/book_hotel.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'booking/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login successful.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('home')
