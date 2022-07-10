from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("wishes", views.wishes),
    path("logout", views.logout),
    path("wishes/new", views.new_wish),
    path("delete_wish/<int:id>/", views.delete_wish),
    path("wishes/edit/<int:id>/", views.edit_wish),
    path("update_wish", views.update_wish),
    path("grant_wish/<int:id>", views.grant_wish),
    path("wishes/stats", views.stats),
    path("like/<int:id>", views.like),
    path("wishes/create_wish", views.create_wish)
]
