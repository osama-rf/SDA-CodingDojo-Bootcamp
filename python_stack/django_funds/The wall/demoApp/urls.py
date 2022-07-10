from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('home',views.home),
    path('home/<int:id>',views.other),
    path('otherHome',views.otherHome),
    path('logout',views.logout),
    path('createPost',views.createPost),
    path('feed',views.feed),
]
