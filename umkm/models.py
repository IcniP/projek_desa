# umkm/models.py
from django.db import models

class UMKM(models.Model):
    STATUS_CHOICES = [
        ('Menunggu Persetujuan', 'Menunggu Persetujuan'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
    ]

    nama_usaha = models.CharField(max_length=200)
    nama_pemilik = models.CharField(max_length=100)
    deskripsi = models.TextField()
    foto_produk = models.ImageField(upload_to='foto_umkm/')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Menunggu Persetujuan')

    def __str__(self):
        return self.nama_usaha