from django.shortcuts import render, get_object_or_404
from .models import Berita

def berita_detail(request, pk):
    berita_utama = get_object_or_404(Berita, pk=pk)
    berita_lainnya = Berita.objects.exclude(pk=pk)[:5]

    context = {
        'berita': berita_utama,
        'berita_lainnya': berita_lainnya
    }
    return render(request, 'berita/berita_detail.html', context)