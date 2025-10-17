# umkm/admin.py

from django.contrib import admin
from .models import UMKM

class UMKMAdmin(admin.ModelAdmin):
    list_display = ('nama_usaha', 'nama_pemilik', 'status')
    list_filter = ('status',)
    search_fields = ('nama_usaha', 'nama_pemilik')
    list_editable = ('status',)

admin.site.register(UMKM, UMKMAdmin)