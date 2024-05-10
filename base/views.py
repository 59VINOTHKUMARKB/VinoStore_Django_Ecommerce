from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer_table
from .forms import UserRegistrationForm
from django.db import connection
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection, transaction
from django.http import HttpResponse
from .models import Products_table,Cart
from datetime import date
from django.utils import timezone

def index(request):
    print('Entered Index')
    return render(request, 'base/index.html')

def product(request):
    print('Entered Product')
    return render(request, 'base/product.html')

def productdetails(request):
    print('Entered ProductDetails')
    return render(request, 'base/productdetails.html')

def productdetails2(request):
    print('Entered ProductDetails')
    return render(request, 'base/productdetails2.html')

def productdetails3(request):
    print('Entered ProductDetails')
    return render(request, 'base/productdetails3.html')

def cart(request):
    print('Entered Cart')
    return render(request, 'base/cart.html')

def games(request):
    print('Entered Games')
    return render(request, 'base/games.html')

def about(request):
    print('Entered About')
    return render(request, 'base/about.html')

def registration(request):
    print('Entered registration form')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            email = request.POST.get('register-email', '')
            location = request.POST.get('location', '')
            age = request.POST.get('age', None)
            print(f"Email: {email}, Location: {location}, Age: {age}")
            customer = Customer_table.objects.create(
                username=user.username,
                email=email,
                password=user.password,
                age=age,
                location=location
            )
            print('Customer object created')
            
            messages.success(request, 'Registration successful', 'register')
            return redirect('app_name:login')
        else:
            messages.error(request, 'Registration failed. Please check the form.', 'register')
    return render(request, 'base/registration.html')

def custom_login(request):
    print('Entered Login form')
    if request.method == 'POST':
        if 'login-username' in request.POST:
            username = request.POST['login-username']
            password = request.POST['login-password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful', 'login')
                return redirect('app_name:index')
            else:
                messages.error(request, 'Invalid login credentials', 'login')
    return render(request, 'base/login.html')

def custom_logout(request):
    print('Entered Logout')
    logout(request)
    return redirect('app_name:index')


def get_cart_items(request):
    print('Entered getCart')
    cart_items = [
        {'id': product.id, 'name': product.product_name, 'price': product.product_price, 'image': product.product_image.url}
        for product in Products_table.objects.all()
    ]
    print('returning Cart items')
    return JsonResponse(cart_items, safe=False)

def product_list(request):
    print('Entered Productlist')
    products = Products_table.objects.all()
    print(products)
    return render(request, 'base/product.html', {'products': products})

def product_list2(request):
    print('Entered Productlist2')
    products = Products_table.objects.all()
    print(products)
    return render(request, 'base/productdetails.html', {'products': products})

def product_list3(request):
    print('Entered Productlist2')
    products = Products_table.objects.all()
    print(products)
    return render(request, 'base/productdetails2.html', {'products': products})

def product_list4(request):
    print('Entered Productlist2')
    products = Products_table.objects.all()
    print(products)
    return render(request, 'base/productdetails3.html', {'products': products})

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cart, Products_table

@login_required
def add_to_cart(request):
    print('ENTER add to cart')
    if request.method == 'POST':
        user = request.user
        print(user)
        if user.is_authenticated:
            print('getting product_id')
            product_id = request.POST.get('product_id')
            print(product_id)
            quantity = int(request.POST.get('quantity', 1))
            print(quantity)
            if not product_id:
                return JsonResponse({'success': False, 'message': 'Product ID is missing or empty.'})

            print('Fetching product using raw SQL query')
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM base_products_table WHERE product_id = %s", [product_id])
                product_row = cursor.fetchone()

            if product_row:
                product = {
                    'product_id': product_row[0],
                    'product_name': product_row[1],
                    'stock': product_row[2],
                    'price': product_row[3]
                }
                print(product)
            else:
                return JsonResponse({'success': False, 'message': 'Product not found.'})
            created_at = timezone.now()
            print('Updating cart table using raw SQL query')
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO base_cart (customer_name,quantity,created_at,product_id) "
                    "VALUES (%s, %s, %s,%s)",
                    [user,quantity,created_at,product_id]
                )

            

            return JsonResponse({'success': True, 'message': 'Product added to cart successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'User is not authenticated.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    
def add_to_order(request):
    print('Entered add to order')
    if request.method == 'POST':
        user = request.user
        print(user)
        if user.is_authenticated:
            print('getting product_id')
            product_id = request.POST.get('product_id')
            print(product_id)
            quantity = int(request.POST.get('quantity', 1))
            print(quantity)
            if not product_id:
                return JsonResponse({'success': False, 'message': 'Product ID is missing or empty.'})

            print('Fetching product using raw SQL query')
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM base_products_table WHERE product_id = %s", [product_id])
                product_row = cursor.fetchone()
                product_name=product_row[1]
                stock=product_row[2]
            if product_row:
                product = {
                    'product_id': product_row[0],
                    'stock': product_row[2],
                    'price': product_row[3]
                }
                print(product)
            else:
                return JsonResponse({'success': False, 'message': 'Product not found.'})
            if stock <= 0:
                return JsonResponse({'success': False, 'message': 'Out of stock.'})
            created_at = timezone.now()
            print('Updating cart table using raw SQL query')
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO base_orderingtable (customer_name,created_at,product_name,product_id_id) "
                    "VALUES (%s, %s, %s,%s)",
                    [user,created_at,product_name,product_id]
                )

            print('Decrementing product stock using raw SQL query')
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE base_products_table SET stock = stock - %s WHERE product_id = %s",
                    [quantity, product_id]
                )
            return JsonResponse({'success': True, 'message': 'Product Ordered successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'User is not authenticated.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

from django.http import JsonResponse
from django.db import connection

def update_rewards_table(request):
    print('Entered rewards view')
    if request.method == 'POST':
        user = request.user
        print(user)
        customer_id = request.user.id
        prize = request.POST.get('prize')
        print(prize)
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM base_rewardstable WHERE customer_name = %s AND rewards = %s",
                    [user, prize]
                )
                existing_reward = cursor.fetchone()

            if existing_reward:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE base_rewardstable SET quantity = quantity + 1 WHERE customer_name = %s AND rewards = %s",
                        [user, prize]
                    )
            else:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO base_rewardstable (customer_name, rewards, quantity) VALUES (%s,%s, 1)",
                        [user, prize]
                    )

            return JsonResponse({'success': True})
        
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    

