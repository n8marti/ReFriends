"""Defines URL patterns for users."""

from django.urls import include, path

from . import views

app_name = "users"

urlpatterns = [
    # Include default auth URLs
    path("", include("django.contrib.auth.urls")),
    # Registration page
    path("register/", views.register, name="register"),
]
