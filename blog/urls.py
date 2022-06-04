from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("blog/<str:post_url>", views.PostView.as_view(), name="post"),
    path("search/tag/<str:tag>", views.search_tag, name="tag"),
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),
    path("<str:page_url>", views.page, name="page")
]
