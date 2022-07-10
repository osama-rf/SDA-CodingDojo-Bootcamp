from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('login',views.login),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('state', views.state),
    path('wish/new', views.new_wish),
    path('wish/create', views.create_wish),
    path('wish/<wish_id>/edit', views.edit_wish),
    path('wish/<wish_id>/update', views.update_wish),
    path('wish/granted/<wish_id>', views.grant),
    path('wish/like/<granted_id>', views.likes),
    path('wish/<job_id>/destroy', views.delete),
    ]
