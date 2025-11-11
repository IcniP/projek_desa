from django.contrib import admin
from .models import DataStatistik, KategoriStatistik 

@admin.register(KategoriStatistik)
class KategoriStatistikAdmin(admin.ModelAdmin):
    list_display = ('nama_kategori',)
    search_fields = ('nama_kategori',)

@admin.register(DataStatistik)
class DataStatistikAdmin(admin.ModelAdmin):
    list_display = ('kategori', 'label', 'jumlah')
    list_filter = ('kategori',) 
    search_fields = ('label', 'kategori__nama_kategori') 
    list_editable = ('jumlah',)