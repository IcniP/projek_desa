# umkm/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_umkm, name='daftar_umkm'),
    path('daftar/', views.pendaftaran_umkm, name='pendaftaran_umkm'),
]