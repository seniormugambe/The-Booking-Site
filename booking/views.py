from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Item, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('item_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
             return redirect('booking:product')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

@login_required
def book_item(request):
    item = get_object_or_404(Item)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.item = item
            booking.user = request.user
            booking.save()
            return redirect('items_list')
    else:
        form = BookingForm()
    return render(request, 'book_item.html', {'form': form, 'item': item})

@login_required
def booking_confirmation(request):
    return render(request, 'booking:confirmation')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('booking:login')