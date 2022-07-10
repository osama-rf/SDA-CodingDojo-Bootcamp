from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('login',views.login),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('jobs/new', views.new_job),
    path('jobs/create', views.create_job),
    path('jobs/<job_id>', views.view_job, name= 'view'),
    path('jobs/add/<job_id>', views.add_job)
]