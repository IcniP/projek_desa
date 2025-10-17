# profil/views.py

from django.shortcuts import render
from .models import Profil  # 1. Pastikan Model diimpor

def index(request):
    # 2. Ambil SEMUA data dari database
    semua_profil = Profil.objects.all()

    # 3. Siapkan data untuk dikirim ke template
    context = {
        'semua_profil': semua_profil,
    }

    # 4. Gunakan 'render' untuk mengirim data ke template HTML
    return render(request, 'profil/index.html', context)