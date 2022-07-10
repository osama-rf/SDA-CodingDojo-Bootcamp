from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('shows',views.all_shows),
    path('shows/new',views.show_new),
    path('shows/create',views.create_show),
    path('shows/<show_id>',views.show),
    path('shows/<show_id>/edit',views.show_edit),
    path('shows/<show_id>/update',views.update_show),
    path('shows/<show_id>/destroy',views.show_destroy),
]
