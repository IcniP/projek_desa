from django.db import models

class KategoriStatistik(models.Model):
    nama_kategori = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Kategori Statistik"
        verbose_name_plural = "Kategori Statistik"

    def __str__(self):
        return self.nama_kategori

class DataStatistik(models.Model):
    
    kategori = models.ForeignKey(
        KategoriStatistik, 
        on_delete=models.CASCADE, 
        related_name='data_statistik'
    ) 
    
    label = models.CharField(max_length=100)
    jumlah = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Data Statistik"
        verbose_name_plural = "Data Statistik"
        unique_together = ('kategori', 'label') 

    def __str__(self):
        return f"{self.kategori.nama_kategori} - {self.label}: {self.jumlah}"