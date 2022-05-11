from django.urls import path
from . import views

urlpatterns = [
    path("reviews", views.reviews, name="reviews"),
    path("new-review", views.ReviewView.as_view(), name="new-review"),
]