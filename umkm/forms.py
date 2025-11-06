# umkm/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import UMKM, Produk, FotoUMKM


class UMKMForm(forms.ModelForm):
    class Meta:
        model = UMKM
        fields = [
            'nama_usaha', 'nama_pemilik', 'deskripsi', 'foto_utama',
            'lokasi', 'kontak_telepon', 'kontak_instagram', 'link_ecommerce'
        ]
        labels = {
            'nama_usaha': 'Nama Usaha / Toko',
            'nama_pemilik': 'Nama Pemilik',
            'deskripsi': 'Deskripsi Singkat Usaha Anda',
            'foto_utama': 'Foto Utama (Foto Terbaik Usaha Anda)',
            'lokasi': 'Alamat / Lokasi Usaha',
            'kontak_telepon': 'Nomor Telepon / WhatsApp',
            'kontak_instagram': 'Instagram (Opsional, cth: @desa.wayhalim)',
            'link_ecommerce': 'Link Toko Online (Opsional, cSshopee/Tokopedia)',
        }


ProdukFormSet = inlineformset_factory(
    UMKM,       
    Produk,     
    fields=('nama_produk', 'deskripsi_produk'), 
    extra=5,    
    can_delete=False 
)


FotoFormSet = inlineformset_factory(
    UMKM,       
    FotoUMKM,   
    fields=('foto', 'keterangan'), 
    extra=5,    
    can_delete=False
)