from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_reg_page),
    path('create_user', views.create_user),
    path('books', views.books_page),
    path('books/add', views.add_book_page),
    path('books/<int:book_id>', views.single_book_page),
    path('create_book', views.create_book),
    path('create_review', views.create_review),
    path('login', views.login),
    path('logout', views.logout),
    path('reviews/<int:review_id>/delete', views.delete_review),
    path('users/<int:user_id>', views.user_page)
]