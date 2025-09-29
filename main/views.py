from django.shortcuts import render, get_object_or_404
from .models import HomepageImage, InfoPageContent, BlogPost, Exhibition, Project, Service


# -------------------------
# Homepage
# -------------------------
def home(request):
    """Home page with image carousel"""
    images = HomepageImage.objects.all()
    return render(request, "main/home.html", {"images": images})


# -------------------------
# Info Page
# -------------------------
def info(request):
    """Info page with Finn’s bio and portrait"""
    info = InfoPageContent.objects.first()
    return render(request, "main/info.html", {"info": info})


# -------------------------
# Blog
# -------------------------
def blog_list_view(request):
    """List view of all blog posts"""
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "main/blog_list.html", {"posts": posts})


def blog_detail_view(request, slug):
    """Detailed view of a single blog post"""
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "main/blog_detail.html", {"post": post})


# -------------------------
# Exhibitions
# -------------------------
def exhibitions(request):
    """List of exhibitions"""
    exhibitions = Exhibition.objects.all().order_by("-date")
    return render(request, "main/exhibitions.html", {"exhibitions": exhibitions})


# -------------------------
# Projects
# -------------------------
def projects(request):
    """Projects page with all projects"""
    projects = Project.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "main/projects.html", {"projects": projects})


# -------------------------
# Services
# -------------------------
def service_detail(request, slug):
    """Generic service detail view"""
    service = get_object_or_404(Service, slug=slug, is_published=True)
    return render(request, "main/service_detail.html", {"service": service})


# Convenience wrappers for fixed URLs
def composer(request):
    return service_detail(request, slug="composer")


def post_production_audio(request):
    return service_detail(request, slug="post-production-audio")


def sound_design(request):
    return service_detail(request, slug="sound-design")


def sound_recordist(request):
    return service_detail(request, slug="sound-recordist")
