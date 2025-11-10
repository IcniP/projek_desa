# umkm/admin.py

from django.contrib import admin, messages
from django.utils.html import format_html
from .models import UMKM, Produk, FotoUMKM


class ProdukInline(admin.TabularInline):
    model = Produk
    extra = 1 

class FotoUMKMInline(admin.TabularInline):
    model = FotoUMKM
    extra = 1 
    fields = ('tampilkan_foto', 'foto', 'keterangan')
    readonly_fields = ('tampilkan_foto',)
    
    def tampilkan_foto(self, obj):
        if obj.foto:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" style="max-height: 100px; border-radius: 4px;" />'
                '</a>',
                obj.foto.url
            )
        return "Belum ada foto"
    tampilkan_foto.short_description = 'Preview Foto'


@admin.register(UMKM)
class UMKMAdmin(admin.ModelAdmin):
    

    list_display = ('nama_usaha', 'tampilkan_foto_utama', 'nama_pemilik', 'status')

    list_filter = ('status',)

    search_fields = ('nama_usaha', 'nama_pemilik')
    
    inlines = [FotoUMKMInline, ProdukInline]
    
    actions = ['setujui_pendaftaran', 'tolak_dan_hapus_pendaftaran', 'hapus_umkm_disetujui']

    @admin.action(description='Setujui Pendaftaran yang Dipilih')
    def setujui_pendaftaran(self, request, queryset):
        updated = queryset.filter(status='Menunggu Persetujuan').update(status='Disetujui')
        self.message_user(request, f'{updated} pendaftaran UMKM berhasil disetujui.', messages.SUCCESS)

    @admin.action(description='Tolak & Hapus Pendaftaran (Menunggu)')
    def tolak_dan_hapus_pendaftaran(self, request, queryset):
        count = queryset.filter(status='Menunggu Persetujuaan').count()
        queryset.filter(status='Menunggu Persetujuan').delete() 
        self.message_user(request, f'{count} pendaftaran (Menunggu) berhasil ditolak dan dihapus.', messages.SUCCESS)

    @admin.action(description='Hapus UMKM (Yang Sudah Disetujui)')
    def hapus_umkm_disetujui(self, request, queryset):
        count = queryset.filter(status='Disetujui').count()
        queryset.filter(status='Disetujui').delete() 
        self.message_user(request, f'{count} UMKM (Disetujui) berhasil dihapus permanen.', messages.WARNING) # Pesan warning agar lebih hati-hati
    
    def tampilkan_foto_utama(self, obj):
        if obj.foto_utama:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" style="max-height: 50px; border-radius: 4px;" />'
                '</a>',
                obj.foto_utama.url
            )
        return "Tidak Ada Foto"
    tampilkan_foto_utama.short_description = 'Foto Utama'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            if request.GET:
                return qs 
            
            return qs.filter(status='Menunggu Persetujuan')
        return qs