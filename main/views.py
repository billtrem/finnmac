from django.shortcuts import render, get_object_or_404
from .models import HomepageImage, InfoPageContent, BlogPost, Exhibition, Project, Service


# -------------------------
# Homepage
# -------------------------
def home(request):
    """
    Home page with image carousel and highlights.
    """
    images = HomepageImage.objects.all().order_by("id")
    latest_posts = BlogPost.objects.all().order_by("-created_at")[:3]

    current_exhibitions = Exhibition.objects.filter(status="current").order_by("date")
    upcoming_exhibitions = Exhibition.objects.filter(status="upcoming").order_by("date")
    past_exhibitions = Exhibition.objects.filter(status="past").order_by("-date")[:3]

    projects = Project.objects.filter(is_published=True).order_by("-created_at")[:4]
    info = InfoPageContent.objects.first()

    context = {
        "images": images,
        "latest_posts": latest_posts,
        "current_exhibitions": current_exhibitions,
        "upcoming_exhibitions": upcoming_exhibitions,
        "past_exhibitions": past_exhibitions,
        "projects": projects,
        "info": info,
    }
    return render(request, "main/home.html", context)


# -------------------------
# Info Page
# -------------------------
def info(request):
    """
    Info page with Finn’s bio, portrait, and contact details.
    """
    info = InfoPageContent.objects.first()

    current_exhibitions = Exhibition.objects.filter(status="current").order_by("date")
    upcoming_exhibitions = Exhibition.objects.filter(status="upcoming").order_by("date")

    projects = Project.objects.filter(is_published=True).order_by("-created_at")[:6]
    services = Service.objects.filter(is_published=True).order_by("created_at")

    context = {
        "info": info,
        "current_exhibitions": current_exhibitions,
        "upcoming_exhibitions": upcoming_exhibitions,
        "projects": projects,
        "services": services,
    }
    return render(request, "main/info.html", context)


# -------------------------
# Blog
# -------------------------
def blog_list_view(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "main/blog_list.html", {"posts": posts})


def blog_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    other_posts = BlogPost.objects.exclude(slug=slug).order_by("-created_at")[:5]

    context = {
        "post": post,
        "other_posts": other_posts,
    }
    return render(request, "main/blog_detail.html", context)


# -------------------------
# Exhibitions
# -------------------------
def exhibitions(request):
    current_exhibitions = Exhibition.objects.filter(status="current").order_by("date")
    upcoming_exhibitions = Exhibition.objects.filter(status="upcoming").order_by("date")
    past_exhibitions = Exhibition.objects.filter(status="past").order_by("-date")

    context = {
        "current_exhibitions": current_exhibitions,
        "upcoming_exhibitions": upcoming_exhibitions,
        "past_exhibitions": past_exhibitions,
    }
    return render(request, "main/exhibitions.html", context)


# -------------------------
# Projects
# -------------------------
def projects(request):
    projects_qs = Project.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "main/projects.html", {"projects": projects_qs})


# -------------------------
# Services (each page has its own template)
# -------------------------

def _service(request, service_name, template_name):
    """
    Loads a Service object based on its `name` field and renders using
    a specific template in /services/.
    """
    service = get_object_or_404(Service, name=service_name, is_published=True)
    all_services = Service.objects.filter(is_published=True).order_by("created_at")

    return render(
        request,
        template_name,
        {"service": service, "all_services": all_services},
    )


def composer(request):
    return _service(request, "composer", "main/services/composer.html")


def post_production_audio(request):
    return _service(
        request,
        "post_production_audio",
        "main/services/post-production-audio.html",
    )


def sound_design(request):
    return _service(
        request,
        "sound_design",
        "main/services/sound-design.html",
    )


def sound_recordist(request):
    return _service(
        request,
        "sound_recordist",
        "main/services/sound-recordist.html",
    )
