# profil/views.py
from django.shortcuts import render, get_object_or_404
from .models import Profil, StrukturOrganisasi, LingkunganRT, Galeri , KategoriLayanan, Layanan
from berita.models import Berita
from django.db.models import Q

def index(request):
    berita_terbaru = Berita.objects.all()[:3]
    context = {'berita_terbaru': berita_terbaru}
    return render(request, 'profil/index.html', context)

def halaman_profil_lengkap(request):
    try:
        tentang_kami = Profil.objects.get(judul__icontains="Tentang Kami")
    except Profil.DoesNotExist:
        tentang_kami = None
    semua_kategori = KategoriLayanan.objects.all()
    semua_pejabat = StrukturOrganisasi.objects.all()

    semua_rt = LingkunganRT.objects.all()

    context = {
        'tentang_kami': tentang_kami,
        'semua_kategori': semua_kategori, 
        'semua_pejabat': semua_pejabat,
        'semua_rt': semua_rt,
    }

    return render(request, 'profil/halaman_profil_lengkap.html', context)

def layanan_detail(request, kategori_id):
    kategori = get_object_or_404(KategoriLayanan, pk=kategori_id)
    daftar_layanan = Layanan.objects.filter(kategori=kategori)

    context = {
        'kategori': kategori,
        'daftar_layanan': daftar_layanan,
    }
    return render(request, 'profil/layanan_detail.html', context)

def galeri(request):
    query = request.GET.get('q')
    semua_berita = Berita.objects.all()
    if query:
        bulan_map = { 'januari': 1, 'februari': 2, 'maret': 3, 'april': 4, 'mei': 5, 'juni': 6, 'juli': 7, 'agustus': 8, 'september': 9, 'oktober': 10, 'november': 11, 'desember': 12 }
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
    context = {'semua_berita': semua_berita, 'query': query}
    return render(request, 'profil/galeri.html', context)

def hubungi_kami(request):
    return render(request, 'profil/hubungi_kami.html')