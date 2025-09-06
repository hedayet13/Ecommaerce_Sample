from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart
from catalog.models import Product
from .models import Order, OrderItem
from .forms import CheckoutForm

def checkout(request):
    cart = Cart(request)
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user = request.user if request.user.is_authenticated else None,
                email = form.cleaned_data["email"],
                shipping_address = form.cleaned_data["shipping_address"],
            )
            for item in cart:
                OrderItem.objects.create(order=order, product=item["product"], quantity=item["quantity"], price=item["product"].price)
            cart.clear()
            messages.success(request, "Order placed! (Payment flow not implemented in demo)")
            return redirect("home")
    else:
        form = CheckoutForm()
    return render(request, "orders/checkout.html", {"cart": cart, "form": form})
