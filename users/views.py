from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer


def index(request):
    return render(request, 'base/index.html')

def product(request):
    return render(request, 'base/product.html')

def productdetails(request):
    return render(request, 'base/productdetails.html')

def cart(request):
    return render(request, 'base/cart.html')

def games(request):
    print('hello')
    return render(request, 'base/games.html')

def about(request):
    return render(request, 'base/about.html')

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
                print("Reg success")
                messages.success(request, 'Registration successful', 'register')
                return redirect('app_name:account')

    return render(request, 'base/account.html')

def custom_logout(request):
    logout(request)
    return redirect('app_name:index')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('register-username')
        email = request.POST.get('register-email')
        password = request.POST.get('register-password')  # Hash password for security

        # Create and save new customer
        customer = Customer.objects.create(
            username=username,
            email=email
        )

        # Success message or redirection logic
        return render(request, 'account.html')  # Example success page
    else:
        # Display registration form
        return render(request, 'account.html')
