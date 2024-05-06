from django.urls import path
from . import views

urlpatterns = [
 path('iletisim/', views.iletisim, name='iletisim'),
 path('submit', views.submit_form, name='submit_form'),
 path('hakkimizda',views.hakkimizda,name='hakkimizda'),

]