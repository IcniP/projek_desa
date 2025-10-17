# umkm/views.py
from django.shortcuts import render
from .models import UMKM

def daftar_umkm(request):
    # Ambil semua objek UMKM, TAPI filter hanya yang statusnya 'Disetujui'
    umkm_disetujui = UMKM.objects.filter(status='Disetujui')

    context = {
        'semua_umkm': umkm_disetujui,
    }
    return render(request, 'umkm/daftar_umkm.html', context)