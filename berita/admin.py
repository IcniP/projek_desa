# berita/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Berita

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tampilkan_gambar', 'tanggal_publikasi')
    list_filter = ('tanggal_publikasi',)
    search_fields = ('judul',)
    
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