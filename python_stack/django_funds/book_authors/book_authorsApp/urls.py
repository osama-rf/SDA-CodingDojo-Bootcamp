from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.createBook),
    path('book/<_id>', views.showBook),
    path('authors', views.authors),
    path('creata', views.createAuthor),
    path('author/<_id>', views.showAuthor),
]