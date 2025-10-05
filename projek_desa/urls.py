# projek_desa/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Tambahkan 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', include('profil.urls')),
    path('', include('profil.urls')),
]