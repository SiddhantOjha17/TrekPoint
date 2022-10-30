from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
import razorpay
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

client = razorpay.Client(auth=(settings.KEY, settings.SECRET))


@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user = request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, "shipping": False}
        cartItems = order['get_cart_items']

    # Razorpay
    # client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    # print("client created")
    # payment = client.order.create({'Amount': order.get_cart_total * 100, "currency": "INR", "payment_capture": "1"})
    # print(payment)
    context = {'items': items, 'order': order, 'cartItems': cartItems}  # , "payment": payment

    return render(request, "cart.html", context)

# def razorpaycheck(request):
#     cart = Order.objects.filter(user = request.user)
#     total_price = 0
#     for item in cart:
#         total_price = total_price + item.product.price * item.quantity
#     return JsonResponse({
#         'total_price': total_price
#     })



def processOrder(request):
    print("Data:", request.body)

    return JsonResponse('Payment Complete!! ', safe=False)


def checkout(request):
    customer = Customer.objects.get(user = request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    print(order.get_cart_total * 100)

    print("client created")
    payment = client.order.create({"amount": int(order.get_cart_total * 100), "currency": "INR", "payment_capture": "1"})
    print(payment)
    order.transaction_id = payment['id']
    order.save()

    context = {'items': items, 'order': order, 'cartItems': cartItems, "payment": payment}

    return render(request, "checkout.html", context)


@csrf_exempt
def updateItem(request):
    print("im in update")
    # if request.method =="POST":
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ', action)
    print("ProductId: ", productId)

    customer = Customer.objects.get(user = request.user)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
        print(orderItem.quantity)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse({"message":"Item was added"}, status=200)



def equipment(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'equipment.html', context)


###################################################################################################
# Authentication


def login_auth(request):
    if request.method == 'POST':
        username = request.POST["Text"]
        password = request.POST["Password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Wrong Credentials")
            return redirect('signup')

    return render(request, 'login.html')


def logout_auth(request):
    logout(request)
    return redirect('home')


def signup_auth(request):
    if request.method == 'POST':
        username = request.POST['Name']
        email = request.POST['email']
        password1 = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password1 == confirmpassword:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    user_model = User.objects.get(username= username)
                    customer = Customer(user = user_model, name=username, email= email)
                    customer.save()
                    print("New User Created")

                    login(request, user)
        return redirect('home')
    return render(request, 'signup.html')  # , context
