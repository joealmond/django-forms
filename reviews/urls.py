from importlib.resources import path
from django import views
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view())
    # path("reviews/<int:id>", views.SingleReviewView.as_view())
    # path("thank-you", views.thank_you)
]
