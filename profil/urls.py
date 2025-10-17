# profil/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='profil_index'),
    path('', views.index, name='homepage'),
    path('profil/<int:pk>/', views.detail_profil, name='detail_profil'),
    path('struktur-organisasi/', views.struktur_organisasi, name='struktur_organisasi'),
    path('lingkungan-rt/', views.daftar_rt, name='daftar_rt'),
    path('galeri/', views.galeri, name='galeri'),
    path('hubungi-kami/', views.hubungi_kami, name='hubungi_kami'),
]