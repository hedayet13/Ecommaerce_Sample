from django.shortcuts import render, get_object_or_404
from .models import Post
def blog_list(request):
    posts = Post.objects.order_by("-created_at")[:12]
    return render(request, "blog/list.html", {"posts": posts})
def blog_detail(request, slug):
    p = get_object_or_404(Post, slug=slug)
    return render(request, "blog/detail.html", {"post": p})
