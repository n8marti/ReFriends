"""Defines URL patterns for users."""

from django.urls import include, path

from . import views

app_name = "users"

urlpatterns = [
    # Custom login page
    path("login/", views.CustomLoginView.as_view(), name="login"),
    # Include default auth URLs
    path("", include("django.contrib.auth.urls")),
    # Registration page
    path("register/", views.register, name="register"),
]
