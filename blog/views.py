from datetime import date
from turtle import pos
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm


def index(request):
    posts = Post.objects.filter(status=2, post_type=1).order_by('-date')[:3]
    return render(request, "index.html", {"posts": posts})


def blog(request):
    posts = Post.objects.filter(post_type=1, status=2).order_by("-date")
    return render(request, "blog.html", {"posts": posts})


def post(request, post_url):
    post = get_object_or_404(Post, url=post_url, status=2)
    return render(request, "post.html", {"post": post, "comment_form": CommentForm})


def page(request, page_url):
    page = get_object_or_404(Post, url=page_url, status=2, post_type=2)
    return render(request, "page.html", {"page": page, "comment_form": CommentForm})
