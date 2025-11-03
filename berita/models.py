from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita_pics/')
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tanggal_publikasi']

    def __str__(self):
        return self.judul