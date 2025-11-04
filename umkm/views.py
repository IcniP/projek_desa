# umkm/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import UMKM, Produk
from .forms import UMKMForm

def daftar_umkm(request):
    query = request.GET.get('q')

    umkm_list = UMKM.objects.filter(status='Disetujui')

    if query:
        umkm_list = umkm_list.filter(
            Q(nama_usaha__icontains=query) |
            Q(produk_list__nama_produk__icontains=query)
        ).distinct() 

    context = {
        'semua_umkm': umkm_list,
        'query': query,
    }
    return render(request, 'umkm/daftar_umkm.html', context)

def umkm_detail(request, pk):
    umkm = get_object_or_404(UMKM, pk=pk, status='Disetujui')

    produk = umkm.produk_list.all()
    foto_gallery = umkm.foto_gallery.all()

    context = {
        'umkm': umkm,
        'produk_list': produk,
        'foto_gallery': foto_gallery,
    }
    return render(request, 'umkm/umkm_detail.html', context)

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