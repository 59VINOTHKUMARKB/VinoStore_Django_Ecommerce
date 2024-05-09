from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'base/index.html')

def product(request):
    return render(request, 'base/product.html')

def productdetails(request):
    return render(request, 'base/productdetails.html')

def cart(request):
    return render(request, 'base/cart.html')

def account(request):
    if request.method == 'POST':
        if 'login-username' in request.POST:
            # Handle login form submission
            username = request.POST['login-username']
            password = request.POST['login-password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful', 'login')
                return redirect('app_name:index')
            else:
                messages.error(request, 'Invalid login credentials', 'login')
        elif 'register-username' in request.POST:
            # Handle register form submission
            username = request.POST['register-username']
            email = request.POST['register-email']
            password = request.POST['register-password']

            # Check if the form is valid
            if not (username and email and password):
                messages.error(request, 'Please fill in all fields', 'register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken', 'register')
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                messages.success(request, 'Registration successful', 'register')
                return redirect('app_name:account')

    return render(request, 'base/account.html')

def games(request):
    return render(request, 'base/games.html')

def about(request):
    return render(request, 'base/about.html')
