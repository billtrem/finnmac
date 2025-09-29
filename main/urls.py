from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("info/", views.info, name="info"),
    path("blog/", views.blog_list_view, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail_view, name="blog_detail"),
    path("exhibitions/", views.exhibitions, name="exhibitions"),
    path("projects/", views.projects, name="projects"),   # updated

    # 🎵 Services
    path("services/composer/", views.composer, name="composer"),
    path("services/post-production-audio/", views.post_production_audio, name="post_production_audio"),
    path("services/sound-design/", views.sound_design, name="sound_design"),
    path("services/sound-recordist/", views.sound_recordist, name="sound_recordist"),
]
