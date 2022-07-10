from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login),
    path('books', views.success),
    path('add_a_book', views.add_a_book),
    path('books/<int:book_id>', views.book_details),
    path('books/<int:book_id>/favorite', views.add_favorite),
    path('books/<int:book_id>/edit', views.edit_book),
    path('books/<int:book_id>/unfavorite', views.unfavorite),
    path('books/<int:book_id>/delete', views.delete_book),
    path('logout', views.logout)
]