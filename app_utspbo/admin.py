from django.contrib import admin
from .models import *
class jurnaladmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis', 'penerbit', 'jumlah_halaman', 'tahun_terbit', 'jumlah_halaman', 'kampus', 'kelompok_ikan', 'nama_latin',  'img']
    search_fields = ['judul', 'penulis']
    list_filter = ['kelompok_ikan', 'judul', 'penerbit']
    list_per_page = 4
admin.site.register(Jurnal, jurnaladmin)
admin.site.register(home)
admin.site.register(koor)
admin.site.register(Kelompok_ikan)
admin.site.register(Kampus)
admin.site.register(nama_latin)
# Register your models here.
