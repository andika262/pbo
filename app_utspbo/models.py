from distutils.command.upload import upload
from django.db import models

class nama_latin(models.Model):
    nama_latinn = models.CharField(max_length=54)
    def __str__(self):
        return self.nama_latinn
class Kelompok_ikan(models.Model):
    nama_ikan = models.CharField(max_length=54)
    def __str__(self):
        return self.nama_ikan

class Kampus(models.Model):
    nama_kampus = models.CharField(max_length=54)
    def __str__(self):
        return self.nama_kampus 

class Jurnal(models.Model):
    judul = models.CharField(max_length=10000)
    penulis = models.CharField(max_length=10000)
    penerbit = models.CharField(max_length=40) #jumlah ganti jd 
    email_penerbit = models.CharField(max_length=40) #jumlah ganti jd halaman
    tahun_terbit = models.IntegerField(null=True) 
    img = models.CharField(null=True, max_length=40)
    jumlah_halaman = models.IntegerField(null=True) #null=true ketika tidak ada isinya bisa jalan
    kampus= models.ForeignKey(Kampus, on_delete=models.CASCADE, null=True)
    kelompok_ikan= models.ForeignKey(Kelompok_ikan, on_delete=models.CASCADE, null=True) 
    nama_latin= models.ForeignKey(nama_latin, on_delete=models.CASCADE, null=True)#cascade itu semisalnya yang class kelompok dihapus, trus nama2 yang sama bakal keapus juga
    def __str__(self):
        return self.judul #biar outputnya cuma muncul judul aja yezh

class koor(models.Model):
    nama       = models.CharField(max_length=255)
    coordX     = models.FloatField(null=True)
    coordY     = models.FloatField(null=True)
    def __str__(self):
        return self.nama

class home(models.Model):
    nama_daerah = models.CharField(max_length=255)
    nama_wisata = models.CharField(max_length=255)
    deskripsi   = models.CharField(max_length=255)
    foto   = models.ImageField('Gambar', null=True, blank=True)
    coord  = models.ForeignKey(koor, on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.nama_daerah
# Create your models here.
