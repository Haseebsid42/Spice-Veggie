from django.contrib.auth.models import User
from decimal import Decimal
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404, redirect
from .models import Product,Vegetable,Fruit
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CheckoutForm
from .models import Order



#Login 
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # or wherever you want to redirect
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

#Logout 
def user_logout(request):
    logout(request)
    return redirect('login')

#signup
def sign_up(request):
    if request.method == 'POST':
        print("POST received")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("Data received:", username, email, password)

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully.")
            return redirect('login')

    return render(request, 'signup.html')



# Create your views here.
def home(request):
    return render(request,'home.html')

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 8)  # Show 6 fruits per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'spices.html', {'page_obj': page_obj})

def vegetable_list(request):
    vegetables = Vegetable.objects.all()
    paginator = Paginator(vegetables, 8)  # Show 6 fruits per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'vegetables.html',{'page_obj':page_obj})

def fruit_list(request):
    fruits = Fruit.objects.all()
    paginator = Paginator(fruits, 8)  # Show 6 fruits per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fruits.html', {'page_obj': page_obj})

#add to cart
def add_to_cart(request, item_type, item_id):
    cart = request.session.get('cart', {})
    item_key = f"{item_type}_{item_id}"
    cart[item_key] = cart.get(item_key, 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')


# View cart
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = Decimal('0.00')

    for key, quantity in cart.items():
        item_type, item_id = key.split('_')
        quantity = int(quantity)

        if item_type == "fruit":
            item = get_object_or_404(Fruit, pk=item_id)
        elif item_type == "vegetable":
            item = get_object_or_404(Vegetable, pk=item_id)
        elif item_type == "product":
            item = get_object_or_404(Product, pk=item_id)
        else:
            continue  # skip unknown item type

        total = item.price * quantity
        subtotal += total
        cart_items.append({
            'item_type': item_type,
            'item': item,
            'quantity': quantity,
            'total': total,
        })

    tax_rate = Decimal('0.08')
    delivery_fee = Decimal('5.00')

    tax = (subtotal * tax_rate).quantize(Decimal('0.01'))
    total = (subtotal + tax + delivery_fee).quantize(Decimal('0.01'))

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'tax': tax,
        'delivery': delivery_fee,
        'total': total,
    })

#Checkout
def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')

    items = []
    subtotal = Decimal('0.00')
    shipping = Decimal('5.00')

    for key, quantity in cart.items():
        item_type, item_id = key.split('_')
        quantity = int(quantity)

        if item_type == "fruit":
            item = get_object_or_404(Fruit, pk=item_id)
        elif item_type == "vegetable":
            item = get_object_or_404(Vegetable, pk=item_id)
        elif item_type == "product":
            item = get_object_or_404(Product, pk=item_id)
        else:
            continue

        line_total = item.price * quantity
        subtotal += line_total

        items.append({
            'name': item.name,
            'description': getattr(item, 'description', ''),
            'image': item.image_url if hasattr(item, 'image_url') and item.image_url else '',
            'price': item.price,
            'quantity': quantity,
            'line_total': line_total,
        })

    total = subtotal + shipping

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        payment_method = request.POST.get('payment_method')

        if full_name and address and phone and payment_method:
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                full_name=full_name,
                address=address,
                phone=phone,
                payment_method=payment_method,
                total=total
            )

            request.session['cart'] = {}

            return render(request, 'order_success.html', {
                'order': order,
                'items': items,
                'subtotal': subtotal,
                'shipping': shipping,
                'total': total
            })

    return render(request, 'checkout.html', {
        'items': items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total
    })

#signup
def sign_up(request):
   return render(request, 'signup.html')
    
    
# Remove from cart
def remove_from_cart(request, fruit_id):
    cart = request.session.get('cart', {})
    if str(fruit_id) in cart:
        del cart[str(fruit_id)]
    request.session['cart'] = cart
    return redirect('view_cart')

#cart increase / decrease
def increase_quantity(request, item_type, item_id):
    cart = request.session.get('cart', {})
    key = f"{item_type}_{item_id}"
    if key in cart:
        cart[key] += 1
    request.session['cart'] = cart
    return redirect('view_cart')


def decrease_quantity(request, item_type, item_id):
    cart = request.session.get('cart', {})
    key = f"{item_type}_{item_id}"
    if key in cart:
        if cart[key] > 1:
            cart[key] -= 1
        else:
            del cart[key]
    request.session['cart'] = cart
    return redirect('view_cart')

#Search 
from django.shortcuts import render
from .models import Product, Fruit, Vegetable

def search_view(request):
    query = request.GET.get('q', '')
    fruits = Fruit.objects.filter(name__icontains=query)
    vegetables = Vegetable.objects.filter(name__icontains=query)
    spices = Product.objects.filter(name__icontains=query)

    results = list(fruits) + list(vegetables) + list(spices)

    return render(request, 'search_results.html', {
        'query': query,
        'results': results,
    })
