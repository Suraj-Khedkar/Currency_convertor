from django.urls import path
from . import views


urlpatterns = [
    path("", views.index ,name='index'),
    path("realtimeconvert",views.calculate ,name='calculate'),
    path("dateconvert",views.dateconvert,name='dateconvert'),
    path("graph",views.graph,name='graph'),
    path("rates",views.rates,name='rates')
]