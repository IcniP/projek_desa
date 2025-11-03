# projek_desa/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings               
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', include('profil.urls')),
    path('', include('profil.urls')),
    path('umkm/', include('umkm.urls')),
    path('berita/', include('berita.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)