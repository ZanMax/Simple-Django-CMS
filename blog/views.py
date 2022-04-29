from datetime import date
from turtle import pos
from django.shortcuts import render

# Create your views here.

posts = [
    {"title": "test title #1 ",
     "date": date(2022, 3, 1),
     "author": "Max",
     "text": "long text #1 ",
     "url": "test-title-1",
     },
    {"title": "test title #2 ",
     "date": date(2022, 3, 3),
     "author": "Jack",
     "text": "long text #2 ",
     "url": "test-title-2",
     },
    {"title": "test title #3 ",
     "date": date(2022, 3, 4),
     "author": "Max",
     "text": "long text #3 ",
     "url": "test-title-3",
     }
]


def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(posts, key=get_date)
    latest = sorted_posts[-3:]
    return render(request, "index.html", {"posts": latest})


def blog(request):
    return render(request, "blog.html", {"posts": posts})


def post(request, post_url):
    post = next(post for post in posts if post['url'] == post_url)
    return render(request, "post.html", {"post": post})
