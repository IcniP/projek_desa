from django.contrib import admin
from .models import UMKM, Produk, FotoUMKM

class ProdukInline(admin.TabularInline):
    model = Produk
    extra = 1 

class FotoUMKMInline(admin.TabularInline):
    model = FotoUMKM
    extra = 1 

@admin.register(UMKM) 
class UMKMAdmin(admin.ModelAdmin):
    list_display = ('nama_usaha', 'nama_pemilik', 'status', 'lokasi')
    list_filter = ('status',)
    search_fields = ('nama_usaha', 'nama_pemilik')
    list_editable = ('status',)
    
    inlines = [FotoUMKMInline, ProdukInline]