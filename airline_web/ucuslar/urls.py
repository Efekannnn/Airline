from django.urls import path
from . import views


urlpatterns = [
    path('', views.anasayfa, name='index'),
    path('/list', views.list_flight, name='list'),
    path('/<int:flight_id>', views.flight, name="flight")
]
