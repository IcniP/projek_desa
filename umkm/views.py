# umkm/views.py
from django.shortcuts import render, redirect 
from .models import UMKM
from .forms import UMKMForm 

def daftar_umkm(request):
    umkm_disetujui = UMKM.objects.filter(status='Disetujui')
    context = {
        'semua_umkm': umkm_disetujui,
    }
    return render(request, 'umkm/daftar_umkm.html', context)

def pendaftaran_umkm(request):
    if request.method == 'POST':
        form = UMKMForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('daftar_umkm') 
    else:
        form = UMKMForm() 
    
    context = {
        'form': form,
    }
    return render(request, 'umkm/pendaftaran_umkm.html', context)