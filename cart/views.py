from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from catalog.models import Product
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})

def cart_add(request, product_id):
    cart = Cart(request)
    qty = 1
    if request.method == "POST":
        try:
            qty = max(1, int(request.POST.get("quantity", "1")))
        except ValueError:
            qty = 1
    cart.add(product_id, quantity=qty)
    messages.success(request, "Added to cart.")
    return redirect(request.META.get("HTTP_REFERER", "cart_detail"))

def cart_update(request, product_id):
    """Override quantity from the cart page."""
    cart = Cart(request)
    try:
        qty = int(request.POST.get("quantity", "1"))
    except ValueError:
        qty = 1
    if qty <= 0:
        cart.remove(product_id)
        messages.info(request, "Item removed.")
    else:
        cart.add(product_id, quantity=qty, override=True)
        messages.success(request, "Quantity updated.")
    return redirect("cart_detail")

def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect("cart_detail")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")
