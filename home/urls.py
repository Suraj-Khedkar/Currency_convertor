from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name='index'),
    path("realtimeconvert",views.calculate ,name='calculate'),
    path("dateconvert",views.dateconvert,name='dateconvert')
]