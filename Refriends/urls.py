"""Defines URL patterns for Refriends."""

from django.urls import path

from . import views

app_name = "Refriends"
urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    # Page that shows all Groups
    path("groups/", views.groups, name="groups"),
    # Detail page for a single group.
    path("groups/<int:group_id>/", views.group, name="group"),
    # Page for adding a new group
    path("new_group/", views.new_group, name="new_group"),
    # Page for posting a new message
    path("new_message/<int:group_id>/", views.new_message, name="new_message"),
    # Info page
    path("info/", views.info, name="info"),
    path("set_timezone/", views.set_timezone, name="set_timezone"),
]
