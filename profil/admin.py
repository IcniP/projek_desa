# profil/admin.py

from django.contrib import admin
from .models import Profil  # Impor model Profil yang sudah kita buat

# Daftarkan model Profil agar muncul di halaman admin
admin.site.register(Profil)