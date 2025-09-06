from django.shortcuts import render, get_object_or_404
from .models import Vendor
from catalog.models import Product

def vendor_detail(request, pk):
    v = get_object_or_404(Vendor, pk=pk)
    products = Product.objects.filter(vendor=v, is_active=True)
    return render(request, "vendors/detail.html", {"vendor": v, "products": products})
