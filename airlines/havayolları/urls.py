from django.urls import path
from .import views 

urlpatterns = [
    path('',views.anasayfa),
    path('search/', views.flight_search, name='flight_search'),  
    path('bilet-al/', views.bilet_al, name='bilet_al'),

]
