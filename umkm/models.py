
from django.db import models

class UMKM(models.Model):
    STATUS_CHOICES = [
        ('Menunggu Persetujuan', 'Menunggu Persetujuan'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
    ]

    nama_usaha = models.CharField(max_length=200)
    nama_pemilik = models.CharField(max_length=100)
    deskripsi = models.TextField(help_text="Deskripsi umum tentang toko/usaha Anda")
    foto_utama = models.ImageField(upload_to='umkm_utama/', help_text="Foto terbaik yang mewakili usaha Anda", blank=True, null=True)
    
    lokasi = models.CharField(max_length=255, blank=True, null=True, help_text="Contoh: Jl. Mawar No. 10")
    link_ecommerce = models.URLField(max_length=255, blank=True, null=True, help_text="Link ke Tokopedia, Shopee, dll.")
    kontak_telepon = models.CharField(max_length=20, blank=True, null=True, help_text="Nomor WhatsApp atau Telepon")
    kontak_instagram = models.CharField(max_length=100, blank=True, null=True, help_text="Nama pengguna Instagram, cth: @desa.wayhalim")

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Menunggu Persetujuan')

    def __str__(self):
        return self.nama_usaha

class Produk(models.Model):
    umkm = models.ForeignKey(UMKM, related_name='produk_list', on_delete=models.CASCADE)
    nama_produk = models.CharField(max_length=200)
    deskripsi_produk = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nama_produk

class FotoUMKM(models.Model):
    umkm = models.ForeignKey(UMKM, related_name='foto_gallery', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='umkm_gallery/')
    keterangan = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Foto untuk {self.umkm.nama_usaha}"