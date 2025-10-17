# umkm/forms.py
from django import forms
from .models import UMKM

class UMKMForm(forms.ModelForm):
    class Meta:
        model = UMKM
        fields = ['nama_usaha', 'nama_pemilik', 'deskripsi', 'foto_produk']