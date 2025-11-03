# profil/admin.py

from django.contrib import admin
from .models import Profil, StrukturOrganisasi, LingkunganRT, Galeri 

admin.site.register(Profil)
admin.site.register(StrukturOrganisasi)
admin.site.register(LingkunganRT)
admin.site.register(Galeri)