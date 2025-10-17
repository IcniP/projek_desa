# umkm/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Path kosong '' berarti ini adalah halaman utama dari app umkm
    path('', views.daftar_umkm, name='daftar_umkm'),
]