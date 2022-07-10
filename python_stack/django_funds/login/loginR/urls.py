from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('success', views.success)
]
