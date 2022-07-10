from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	   
    path('register', views.register),	   
    path('login', views.login),	   
    path('signout', views.signout),	   
    path('success', views.success),	   
    path('user_profile', views.user_profile),	   
    path('add/<int:id>', views.add),	   
    path('movie_profile/<int:id>', views.movie_profile),	   
    path('like/<int:id>', views.like),	   
    path('dislike/<int:id>', views.dislike),   
]