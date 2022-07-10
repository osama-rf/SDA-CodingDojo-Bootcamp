from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('remove/<int:id>', views.remove),
    path('delete/<int:id>', views.delete)
]
