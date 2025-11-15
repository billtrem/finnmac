from django.shortcuts import render, get_object_or_404
from django.utils.html import linebreaks
from .models import HomepageImage, InfoPageContent, BlogPost, Exhibition, Project, Service


# -------------------------
# Homepage
# -------------------------
def home(request):
    images = HomepageImage.objects.all().order_by("id")
    latest_posts = BlogPost.objects.all().order_by("-created_at")[:3]

    # Format descriptions for exhibitions
    def fmt_exhibitions(qs):
        for ex in qs:
            ex.description_html = linebreaks(ex.description)
        return qs

    current_exhibitions = fmt_exhibitions(
        Exhibition.objects.filter(status="current").order_by("date")
    )
    upcoming_exhibitions = fmt_exhibitions(
        Exhibition.objects.filter(status="upcoming").order_by("date")
    )
    past_exhibitions = fmt_exhibitions(
        Exhibition.objects.filter(status="past").order_by("-date")[:3]
    )

    # Projects formatted
    projects = Project.objects.filter(is_published=True).order_by("-created_at")[:4]
    for p in projects:
        p.description_html = linebreaks(p.description)

    info = InfoPageContent.objects.first()
    if info and info.bio:
        info.bio_html = linebreaks(info.bio)

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
    info = InfoPageContent.objects.first()
    if info and info.bio:
        info.bio_html = linebreaks(info.bio)

    current_exhibitions = Exhibition.objects.filter(status="current").order_by("date")
    upcoming_exhibitions = Exhibition.objects.filter(status="upcoming").order_by("date")

    # Format exhibition descriptions
    for ex in current_exhibitions:
        ex.description_html = linebreaks(ex.description)
    for ex in upcoming_exhibitions:
        ex.description_html = linebreaks(ex.description)

    # Format project descriptions
    projects = Project.objects.filter(is_published=True).order_by("-created_at")[:6]
    for p in projects:
        p.description_html = linebreaks(p.description)

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

    # Apply linebreak formatting
    post.body_html = linebreaks(post.body)

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

    for ex in list(current_exhibitions) + list(upcoming_exhibitions) + list(past_exhibitions):
        ex.description_html = linebreaks(ex.description)

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

    for p in projects_qs:
        p.description_html = linebreaks(p.description)

    return render(request, "main/projects.html", {"projects": projects_qs})


# -------------------------
# Services (each page has its own template)
# -------------------------
def _service(request, service_name, template_name):
    service = get_object_or_404(Service, name=service_name, is_published=True)

    # Apply formatting
    service.description_html = linebreaks(service.description)
    service.process_html = linebreaks(service.process) if service.process else ""
    service.areas_html = linebreaks(service.areas_of_work) if service.areas_of_work else ""

    all_services = Service.objects.filter(is_published=True).order_by("created_at")

    return render(
        request,
        template_name,
        {
            "service": service,
            "all_services": all_services,
        },
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
