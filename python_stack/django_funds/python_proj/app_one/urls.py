from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wishes', views.wishes),
    path('wishes/new', views.new),
    path('wishes/create', views.create),
    path('wishes/edit/<int:wish_id>', views.edit),
    path('wishes/update/<int:wish_id>', views.update),
    path('wishes/delete/<int:wish_id>', views.delete),
    path('wishes/grant/<int:wish_id>', views.grant),
    # path('wishes/like/<int:wish_id>', views.like),
    path('logout', views.logout),
]