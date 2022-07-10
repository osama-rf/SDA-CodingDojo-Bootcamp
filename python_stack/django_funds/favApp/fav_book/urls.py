from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('addBook', views.add_book),
    path('likebook/<book_id>',views.like_book),
    path('books/<book_id>',views.show_book),
    path('unlikebook/<book_id>',views.unlike_book),
    path('update_book/<book_id>',views.update_book),
    path('delete_book/<book_id>',views.delete_book),
]
