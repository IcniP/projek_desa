

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pandas as pd
from .models import DataStatistik, KategoriStatistik 
from .forms import UploadExcelForm


def tampilkan_statistik(request):
    """
    View untuk menampilkan halaman HTML utama dengan chart.
    """
    kategori_list = KategoriStatistik.objects.all().order_by('nama_kategori')

    context = {
        'kategori_list': kategori_list,
        'kategori_json': json.dumps([k.nama_kategori for k in kategori_list]) 
    }
    return render(request, 'statistik/tampil_data.html', context)


def get_data_statistik(request):
    """
    API endpoint untuk diambil oleh JavaScript (Fetch/AJAX).
    """
    kategori_nama = request.GET.get('kategori')
    
    data_query = DataStatistik.objects.all()

    if not kategori_nama:
        kategori_pertama = KategoriStatistik.objects.first()
        if kategori_pertama:
            data = data_query.filter(kategori=kategori_pertama).order_by('id')
        else:
            data = []
    else:
        data = data_query.filter(kategori__nama_kategori=kategori_nama).order_by('id')

    labels = [item.label for item in data]
    dataset = [item.jumlah for item in data]
    
    return JsonResponse({
        'labels': labels,
        'data': dataset,
    })


def is_admin(user):
    return user.is_superuser or user.is_staff

@login_required
@user_passes_test(is_admin) 
def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                df = pd.read_excel(file)
                
                
                for _, row in df.iterrows():
                    kategori_label = row['Kategori']
                    label_data = row['Label']
                    jumlah_data = row['Jumlah']

                    kategori_obj, created = KategoriStatistik.objects.get_or_create(
                        nama_kategori=kategori_label
                    )
                    
                    DataStatistik.objects.update_or_create(
                        kategori=kategori_obj,
                        label=label_data,
                        defaults={'jumlah': jumlah_data}
                    )
                
                messages.success(request, 'Data dari Excel berhasil di-upload dan diproses.')
                return redirect('statistik:tampil_statistik') 

            except Exception as e:
                messages.error(request, f'Terjadi error saat memproses file: {e}')
    else:
        form = UploadExcelForm()
    
    return render(request, 'statistik/upload.html', {'form': form})