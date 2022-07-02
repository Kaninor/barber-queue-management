from django.urls import path

from . import views

urlpatterns = [
    path('panel/barber', views.index)
]
