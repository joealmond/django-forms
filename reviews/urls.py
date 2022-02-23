from importlib.resources import path
from django import views
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.thank_you)
]
