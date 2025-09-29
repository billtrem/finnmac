from django.shortcuts import render, get_object_or_404
from .models import HomepageImage, InfoPageContent, BlogPost, Exhibition, Product


def home(request):
    """Home page with image carousel"""
    images = HomepageImage.objects.all()
    return render(request, "main/home.html", {"images": images})


def info(request):
    """Info page with Finn’s bio and portrait"""
    info = InfoPageContent.objects.first()
    return render(request, "main/info.html", {"info": info})


def blog_list_view(request):
    """List view of all blog posts"""
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "main/blog_list.html", {"posts": posts})


def blog_detail_view(request, slug):
    """Detailed view of a single blog post"""
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "main/blog_detail.html", {"post": post})


def exhibitions(request):
    """List of exhibitions"""
    exhibitions = Exhibition.objects.all().order_by("-date")
    return render(request, "main/exhibitions.html", {"exhibitions": exhibitions})


def shop(request):
    """Shop page with products"""
    products = Product.objects.filter(is_available=True)
    return render(request, "main/shop.html", {"products": products})
