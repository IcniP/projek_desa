from django.urls import path
from . import views

app_name = 'statistik' 

urlpatterns = [
    path('', views.tampilkan_statistik, name='tampil_statistik'),
    path('api/get-data/', views.get_data_statistik, name='get_data_statistik'),
    path('upload/', views.upload_excel, name='upload_excel'),
]