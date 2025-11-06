# umkm/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.db import transaction
from .models import UMKM, Produk    
from .forms import UMKMForm, ProdukFormSet, FotoFormSet

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
        produk_formset = ProdukFormSet(request.POST, prefix='produk')
        foto_formset = FotoFormSet(request.POST, request.FILES, prefix='foto')

        if form.is_valid() and produk_formset.is_valid() and foto_formset.is_valid():

            with transaction.atomic():
                umkm_instance = form.save(commit=False)
                umkm_instance.status = 'Menunggu Persetujuan'
                umkm_instance.save() 

                produk_formset.instance = umkm_instance
                foto_formset.instance = umkm_instance

                produk_formset.save()
                foto_formset.save()

            return redirect('daftar_umkm')
        else:
   
            print("Form tidak valid:", form.errors, produk_formset.errors, foto_formset.errors)

    else:

        form = UMKMForm()
        produk_formset = ProdukFormSet(prefix='produk')
        foto_formset = FotoFormSet(prefix='foto')

    context = {
        'form': form,
        'produk_formset': produk_formset,
        'foto_formset': foto_formset,
    }
    return render(request, 'umkm/pendaftaran_umkm.html', context)