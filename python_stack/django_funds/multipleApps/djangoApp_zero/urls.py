from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name="index"),	   
    path('blogs/new', views.new, name="new"),
    path('create', views.create, name=""),
    path('show/<num>', views.show),
    path('<num>/edit', views.edit),
    path('<num>/delete', views.destroy)
]