# profil/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('profil-desa/', views.halaman_profil_lengkap, name='profil_lengkap'),
    path('pelayanan/<int:kategori_id>/', views.layanan_detail, name='layanan_detail'),
    path('galeri/', views.galeri, name='galeri'),
    path('hubungi-kami/', views.hubungi_kami, name='hubungi_kami'),
]