from datetime import date
from turtle import pos
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.filter(status=2, post_type=1).order_by('-date')[0:3]
    return render(request, "index.html", {"posts": posts})


def blog(request):
    posts = Post.objects.filter(post_type=1)
    return render(request, "blog.html", {"posts": posts})


def post(request, post_url):
    post = Post.objects.get(url=post_url)
    return render(request, "post.html", {"post": post})


def page(request, page_url):
    page = Post.objects.get(url=page_url, status=2, post_type=2)
    return render(request, "page.html", {"page": page})
