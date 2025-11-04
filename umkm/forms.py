# umkm/forms.py
from django import forms
from .models import UMKM

class UMKMForm(forms.ModelForm):
    class Meta:
        model = UMKM

        # Tentukan field mana saja yang ingin ditampilkan di form
        # Kita sertakan semua field baru yang Anda minta
        fields = [
            'nama_usaha', 
            'nama_pemilik', 
            'deskripsi', 
            'foto_utama',    # Menggantikan 'foto_produk' yang lama
            'lokasi', 
            'kontak_telepon', 
            'kontak_instagram', 
            'link_ecommerce'
        ]

        # (Opsional) Memberi label yang lebih ramah pengguna
        labels = {
            'nama_usaha': 'Nama Usaha / Toko',
            'nama_pemilik': 'Nama Pemilik',
            'deskripsi': 'Deskripsi Singkat Usaha Anda',
            'foto_utama': 'Foto Utama (Foto Terbaik Usaha Anda)',
            'lokasi': 'Alamat / Lokasi Usaha',
            'kontak_telepon': 'Nomor Telepon / WhatsApp',
            'kontak_instagram': 'Instagram (Opsional, cth: @desa.wayhalim)',
            'link_ecommerce': 'Link Toko Online (Opsional, cth: Shopee/Tokopedia)',
        }

        # (Opsional) Memberi teks bantuan
        help_texts = {
            'deskripsi': 'Jelaskan secara singkat apa yang Anda jual atau lakukan.',
            'foto_utama': 'Foto ini akan tampil sebagai gambar utama di katalog.',
        }

# Kita tidak memasukkan 'status' karena default-nya sudah 'Menunggu Persetujuan'
# Kita tidak memasukkan 'List Produk' dan 'Galeri Foto' di form ini,
# karena itu akan ditambahkan oleh Admin setelah pendaftaran disetujui.