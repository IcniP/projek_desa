from django.db import models

class Profil(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()

    def __str__(self):
        return self.judul
    
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
    
class StrukturOrganisasi(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    nip = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='struktur_organisasi/', blank=True, null=True)

    def __str__(self):
        return f"{self.nama} - {self.jabatan}"

class LingkunganRT(models.Model):
    nama_lingkungan = models.CharField(max_length=100)
    nomor_rt = models.CharField(max_length=5)
    nama_ketua_rt = models.CharField(max_length=100)

    def __str__(self):
        return f"RT {self.nomor_rt} - {self.nama_lingkungan}"

class Galeri(models.Model):
    keterangan = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to='galeri/')

    def __str__(self):
        return self.keterangan
    
class KategoriLayanan(models.Model):
    nama_kategori = models.CharField(max_length=100)
    # Kita pakai TextField untuk menyimpan kode SVG ikon
    icon_svg = models.TextField(blank=True, null=True, help_text="Tempelkan kode SVG ikon di sini")

    class Meta:
        verbose_name_plural = "Kategori Layanan"

    def __str__(self):
        return self.nama_kategori

class Layanan(models.Model):
    kategori = models.ForeignKey(KategoriLayanan, related_name='layanan_list', on_delete=models.CASCADE)
    nama_layanan = models.CharField(max_length=200)
    deskripsi_lengkap = models.TextField()

    class Meta:
        verbose_name_plural = "Layanan"

    def __str__(self):
        return self.nama_layanan