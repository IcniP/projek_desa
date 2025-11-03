# profil/views.py
from django.shortcuts import render 
from .models import Profil, StrukturOrganisasi, LingkunganRT, Galeri
from berita.models import Berita

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
    semua_foto = Galeri.objects.all()
    context = {'semua_foto': semua_foto}
    return render(request, 'profil/galeri.html', context)

def hubungi_kami(request):
    return render(request, 'profil/hubungi_kami.html')
