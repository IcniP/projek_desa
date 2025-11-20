# profil/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profil, StrukturOrganisasi, LingkunganRT, Galeri,
    KategoriLayanan, Layanan  
)

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('judul',)
    search_fields = ('judul',)

@admin.register(StrukturOrganisasi)
class StrukturOrganisasiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'nip', 'tampilkan_foto')
    search_fields = ('nama', 'jabatan', 'nip')

    def tampilkan_foto(self, obj):
        if obj.foto:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" style="max-height: 50px; border-radius: 4px;" />'
                '</a>',
                obj.foto.url
            )
        return "Tidak Ada Foto"
    tampilkan_foto.short_description = 'Foto'

@admin.register(LingkunganRT)
class LingkunganRTAdmin(admin.ModelAdmin):
    list_display = ('nama_lingkungan', 'nomor_rt', 'nama_ketua_rt')
    list_filter = ('nama_lingkungan',)
    search_fields = ('nama_lingkungan', 'nomor_rt', 'nama_ketua_rt')

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('keterangan', 'tampilkan_gambar')
    search_fields = ('keterangan',)

    def tampilkan_gambar(self, obj):
        if obj.gambar:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" style="max-height: 50px; border-radius: 4px;" />'
                '</a>',
                obj.gambar.url
            )
        return "Tidak Ada Foto"
    tampilkan_gambar.short_description = 'Gambar'


@admin.register(KategoriLayanan)
class KategoriLayananAdmin(admin.ModelAdmin):
    list_display = ('nama_kategori',)

@admin.register(Layanan)
class LayananAdmin(admin.ModelAdmin):
    list_display = ('nama_layanan', 'kategori')
    list_filter = ('kategori',)
    search_fields = ('nama_layanan',)