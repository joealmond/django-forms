from importlib.resources import path
from django import views
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path("", views.review),
    path("thank-you", views.thank_you)
]
