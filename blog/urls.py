from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("blog/<str:post_url>", views.post, name="post"),
    path("<str:page_url>", views.page, name="page")
]