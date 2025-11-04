# profil/views.py
from django.shortcuts import render 
from .models import Profil, StrukturOrganisasi, LingkunganRT, Galeri
from berita.models import Berita
from django.db.models import Q

def index(request):
    semua_profil = Profil.objects.all()
    berita_terbaru = Berita.objects.all()[:3]
    context = {
        'semua_profil': semua_profil,
        'berita_terbaru': berita_terbaru,
    }
    return render(request, 'profil/index.html', context)

def detail_profil(request, pk):
    profil_obj = Profil.objects.get(pk=pk)
    context = {'profil': profil_obj}
    return render(request, 'profil/detail_profil.html', context)

def struktur_organisasi(request):
    semua_pejabat = StrukturOrganisasi.objects.all()
    context = {'semua_pejabat': semua_pejabat}
    return render(request, 'profil/struktur_organisasi.html', context)

def daftar_rt(request):
    semua_rt = LingkunganRT.objects.all()
    context = {'semua_rt': semua_rt}
    return render(request, 'profil/daftar_rt.html', context)

def galeri(request):
    query = request.GET.get('q')
    semua_berita = Berita.objects.all() 

    if query:

        bulan_map = {
            'januari': 1, 'februari': 2, 'maret': 3, 'april': 4,
            'mei': 5, 'juni': 6, 'juli': 7, 'agustus': 8,
            'september': 9, 'oktober': 10, 'november': 11, 'desember': 12
        }

        query_lower = query.lower() 
        filters = Q(judul__icontains=query)
        if query.isdigit():
            query_int = int(query)
            if 1 <= query_int <= 12:
                filters |= Q(tanggal_publikasi__month=query_int)
            if 1900 <= query_int <= 2100: 
                filters |= Q(tanggal_publikasi__year=query_int)

        if query_lower in bulan_map:
            filters |= Q(tanggal_publikasi__month=bulan_map[query_lower])
        semua_berita = semua_berita.filter(filters)

    context = {
        'semua_berita': semua_berita,
        'query': query,
    }
    return render(request, 'profil/galeri.html', context)

def hubungi_kami(request):
    return render(request, 'profil/hubungi_kami.html')
