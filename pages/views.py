from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Page

def page_detail(request, slug):
    p = get_object_or_404(Page, slug=slug)
    return render(request, "pages/page.html", {"page": p})

def contact(request):
    if request.method == "POST":
        messages.success(request, "Thanks! We'll get back to you soon.")
    return render(request, "pages/contact.html")
