from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("info/", views.info, name="info"),
    path("blog/", views.blog_list_view, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail_view, name="blog_detail"),
    path("exhibitions/", views.exhibitions, name="exhibitions"),
    path("shop/", views.shop, name="shop"),
]
