from django.shortcuts import render
from .models import PageImage

def home(request):
    """Render the one-page site with the uploaded image"""
    image = PageImage.objects.first()  # fetch the first uploaded image
    return render(request, "main/home.html", {"image": image})
