from django.db.models import Q, Avg, Count, Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

from .models import Product, Category, ProductImage, Review


def home(request):
    featured = Product.objects.filter(is_active=True).prefetch_related("images").order_by("-created_at")[:12]
    categories = Category.objects.all()[:12]
    latest_products = Product.objects.filter(is_active=True).prefetch_related("images").order_by("-created_at")[:6]
    recommended = Product.objects.filter(is_active=True).prefetch_related("images").order_by("?")[:12]
    articles = []  # plug your blog posts here
    return render(request, "catalog/home.html", {
        "featured": featured,
        "categories": categories,
        "latest_products": latest_products,
        "recommended": recommended,
        "articles": articles,
    })



def product_list(request):
    q = (request.GET.get("q", "")).strip()
    products = Product.objects.filter(is_active=True)
    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
    return render(request, "catalog/product_list.html", {"products": products, "q": q})


def product_detail(request, slug):
    p = (
        Product.objects
        .prefetch_related(Prefetch("images", queryset=ProductImage.objects.all()),
                          "reviews")
        .select_related("category", "vendor")
        .get(slug=slug, is_active=True)
    )

    # Add review: only for authenticated users, name comes from account
    if request.method == "POST" and request.POST.get("form_id") == "add_review":
        if not request.user.is_authenticated:
            messages.warning(request, "Please log in to write a review.")
            login_url = reverse("login")
            return redirect(f"{login_url}?next={p.get_absolute_url()}#reviews")

        display_name = (request.user.get_full_name() or request.user.username).strip()
        body = (request.POST.get("body") or "").strip()
        try:
            rating = int(request.POST.get("rating", "5"))
        except ValueError:
            rating = 5
        rating = max(1, min(5, rating))

        Review.objects.create(product=p, name=display_name, rating=rating, body=body)
        messages.success(request, "Thanks! Your review has been submitted.")
        return redirect(p.get_absolute_url() + "#reviews")

    # Rating summary
    rating_stats = p.reviews.aggregate(avg=Avg("rating"), cnt=Count("id"))
    avg_rating = rating_stats["avg"] or 0
    review_count = rating_stats["cnt"]
    full_stars = int(avg_rating)                 # 0..5
    half_star = (avg_rating - full_stars) >= 0.5 # True/False

    # Related products (same category)
    related = (
        Product.objects.filter(is_active=True, category=p.category)
        .exclude(id=p.id)
        .prefetch_related("images")[:12]
    )

    # Overview/specs from variations (optional)
    specs = []
    try:
        seen = set()
        for v in p.variations.all():
            for av in v.attributes.all():
                label = f"{av.attribute.name}: {av.value}"
                if label not in seen:
                    seen.add(label)
                    specs.append(label)
    except Exception:
        pass

    return render(request, "catalog/product_detail.html", {
    "p": p,
    "avg_rating": avg_rating,
    "review_count": review_count,
    "related": related,
    "specs": specs,
    "full_stars": full_stars,
    "half_star": half_star,
})


def category_detail(request, slug):
    c = get_object_or_404(Category, slug=slug)
    products = c.products.filter(is_active=True)
    return render(request, "catalog/category_detail.html", {"category": c, "products": products})
