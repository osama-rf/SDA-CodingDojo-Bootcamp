from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('wishes/new', views.new_wish),
    path('wishes/create', views.create_wish),
    path('wishes/like_wish/<int:wish_id>', views.like_wish),
    path('wishes/delete_like/<int:wish_id>', views.delete_like),
    path('wishes/<int:id>/delete', views.destroy),
    path('wishes/edit/<int:id>', views.edit_wish),
    path('wishes/update/<int:id>', views.update),
    path('wishes/grant/<int:wish_id>', views.grant),
    path('wishes/stats', views.stats),
    path('log_out', views.log_out),
]