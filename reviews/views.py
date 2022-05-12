from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from reviews.forms import ReviewForm
from .models import Reviews

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "new-review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")


def reviews(request):
    reviews = Reviews.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
