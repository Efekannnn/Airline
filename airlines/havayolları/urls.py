from django.urls import path
from .import views 

urlpatterns = [
    path('',views.anasayfa),
    path('search/', views.flight_search, name='flight_search'),  
    path('bilet-kaydet/', views.bilet_kaydet, name='bilet_kaydet'),  
]