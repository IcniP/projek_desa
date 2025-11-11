# Buka file: statistik/views.py
# Ganti SELURUH isinya dengan ini:

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import pandas as pd

# Import model baru Anda
from .models import DataStatistik, KategoriStatistik 
from .forms import UploadExcelForm


def tampilkan_statistik(request):
    """
    View untuk menampilkan halaman HTML utama dengan chart.
    """
    # Ambil daftar kategori dari model KategoriStatistik (ini kode barunya)
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
    # Ambil parameter 'kategori' (ini sekarang berupa nama, misal "Pendidikan")
    kategori_nama = request.GET.get('kategori')
    
    data_query = DataStatistik.objects.all()

    if not kategori_nama:
        # Jika tidak ada parameter, ambil default (kategori pertama)
        kategori_pertama = KategoriStatistik.objects.first()
        if kategori_pertama:
            data = data_query.filter(kategori=kategori_pertama).order_by('id')
        else:
            data = [] # Database masih kosong
    else:
        # Filter berdasarkan relasi ForeignKey (ini kode barunya)
        data = data_query.filter(kategori__nama_kategori=kategori_nama).order_by('id')

    # Format data untuk Chart.js (ini tidak berubah)
    labels = [item.label for item in data]
    dataset = [item.jumlah for item in data]
    
    return JsonResponse({
        'labels': labels,
        'data': dataset,
    })

# --- Fungsi untuk Cek Admin ---
def is_admin(user):
    return user.is_superuser or user.is_staff

# --- View untuk Upload Excel (jika Anda sudah membuatnya) ---
# Jika Anda belum membuat file/view ini, Anda boleh menghapus fungsi di bawah ini
@login_required
@user_passes_test(is_admin) # Hanya superuser/staff yang bisa akses
def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                df = pd.read_excel(file)
                
                # Asumsi Excel punya kolom: 'Kategori', 'Label', 'Jumlah'
                
                for _, row in df.iterrows():
                    kategori_label = row['Kategori']
                    label_data = row['Label']
                    jumlah_data = row['Jumlah']

                    # Cari atau buat kategori (ini kode barunya)
                    kategori_obj, created = KategoriStatistik.objects.get_or_create(
                        nama_kategori=kategori_label
                    )
                    
                    # Update atau buat data baru (ini kode barunya)
                    DataStatistik.objects.update_or_create(
                        kategori=kategori_obj,
                        label=label_data,
                        defaults={'jumlah': jumlah_data}
                    )
                
                messages.success(request, 'Data dari Excel berhasil di-upload dan diproses.')
                return redirect('statistik:tampil_statistik') # Arahkan ke halaman chart

            except Exception as e:
                messages.error(request, f'Terjadi error saat memproses file: {e}')
    else:
        form = UploadExcelForm()
    
    return render(request, 'statistik/upload.html', {'form': form})