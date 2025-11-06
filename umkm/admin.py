# umkm/admin.py

from django.contrib import admin, messages
from django.utils.html import format_html
from .models import UMKM, Produk, FotoUMKM

# --- Inlines (Tidak berubah dari sebelumnya) ---

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

# --- Kustomisasi Admin Utama (Sudah Termasuk Permintaan Anda) ---
@admin.register(UMKM)
class UMKMAdmin(admin.ModelAdmin):
    
    # Kolom yang tampil
    list_display = ('nama_usaha', 'tampilkan_foto_utama', 'nama_pemilik', 'status')
    
    # Filter di sidebar kanan
    list_filter = ('status',)
    
    # Search bar
    search_fields = ('nama_usaha', 'nama_pemilik')
    
    # Inlines (Produk & Foto)
    inlines = [FotoUMKMInline, ProdukInline]
    
    # 1. Daftarkan SEMUA Actions (Termasuk action baru Anda)
    actions = ['setujui_pendaftaran', 'tolak_dan_hapus_pendaftaran', 'hapus_umkm_disetujui']

    # --- FUNGSI ACTIONS ---
    @admin.action(description='Setujui Pendaftaran yang Dipilih')
    def setujui_pendaftaran(self, request, queryset):
        # Kita hanya setujui yang statusnya masih 'Menunggu'
        updated = queryset.filter(status='Menunggu Persetujuan').update(status='Disetujui')
        self.message_user(request, f'{updated} pendaftaran UMKM berhasil disetujui.', messages.SUCCESS)

    @admin.action(description='Tolak & Hapus Pendaftaran (Menunggu)')
    def tolak_dan_hapus_pendaftaran(self, request, queryset):
        # Kita hanya hapus yang statusnya 'Menunggu'
        count = queryset.filter(status='Menunggu Persetujuaan').count()
        queryset.filter(status='Menunggu Persetujuan').delete() 
        self.message_user(request, f'{count} pendaftaran (Menunggu) berhasil ditolak dan dihapus.', messages.SUCCESS)

    # === INI ADALAH FUNGSI BARU UNTUK PERMINTAAN ANDA ===
    @admin.action(description='Hapus UMKM (Yang Sudah Disetujui)')
    def hapus_umkm_disetujui(self, request, queryset):
        # Kita hanya hapus yang statusnya 'Disetujui'
        count = queryset.filter(status='Disetujui').count()
        queryset.filter(status='Disetujui').delete() 
        self.message_user(request, f'{count} UMKM (Disetujui) berhasil dihapus permanen.', messages.WARNING) # Pesan warning agar lebih hati-hati
    
    # --- FUNGSI PREVIEW FOTO ---
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

    # 2. INI ADALAH FUNGSI UNTUK PERMINTAAN 'DEFAULT' ANDA
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # Cek jika ada filter aktif di URL (misal: ?status__exact=Disetujui)
            if request.GET:
                return qs # Jika ada filter, tampilkan sesuai filter
            
            # Jika tidak ada filter (tampilan default),
            # tampilkan yang 'Menunggu Persetujuan'
            return qs.filter(status='Menunggu Persetujuan')
        return qs