from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from .forms import CommentForm
from .models import Post, Tags


def index(request):
    posts = Post.objects.filter(status=2, post_type=1).order_by('-date')[:3]
    return render(request, "index.html", {"posts": posts})


def blog(request):
    posts = Post.objects.filter(post_type=1, status=2).order_by("-date")
    return render(request, "blog.html", {"posts": posts})


def post(request, post_url):
    post = get_object_or_404(Post, url=post_url, status=2)
    tags = post.tags.all()
    return render(request, "post.html", {"post": post, "tags": tags, "comment_form": CommentForm})


def page(request, page_url):
    page = get_object_or_404(Post, url=page_url, status=2, post_type=2)
    tags = page.tags.all()
    return render(request, "page.html", {"page": page, "tags": tags, "comment_form": CommentForm})


def search_tag(request, tag):
    tags = Tags.objects.all()
    # posts = Post.objects.filter(status=2).order_by("-date")
    print(tag)
    # posts = Post.objects.values('tags__tag', 'url', 'title', 'date', 'author__first_name', 'text').filter(status=2, tags__tag=tag).order_by("-date")
    posts = Post.objects.values('tags__tag', 'url', 'title', 'date', 'author__first_name', 'text')
    f_posts = posts.filter(tags__tag='math', status=2).values()
    print(f_posts)
    return render(request, "search.html", {"posts": f_posts, "tag": tag, "tags": tags})


class PostView(View):
    def get(self, request, post_url):
        post_detail = get_object_or_404(Post, url=post_url, status=2)
        context = {"post": post_detail,
                   "tags": post_detail.tags.all(),
                   "comment_form": CommentForm}
        return render(request, "post.html", context)

    def post(self, request, post_url):
        comment_form = CommentForm(request.POST)
        post_detail = get_object_or_404(Post, url=post_url, status=2)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post_id = post_detail
            comment.save()
            return HttpResponseRedirect(reverse('post', args=[post_url]))

        context = {"post": post_detail,
                   "tags": post_detail.tags.all(),
                   "comment_form": CommentForm}
        return render(request, "post.html", context)
