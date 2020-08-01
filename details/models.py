import uuid
from django.db import models
from django.utils.text import slugify
class pembeli_unconfirm (models.Model):
    kode = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    nama_pembeli = models.CharField(max_length=25)
    nama_hewan = models.CharField(max_length=25)
    nama_toko = models.CharField(max_length=25)
    jumlah_pesan = models.IntegerField()
    harga_pesan = models.IntegerField()
    total_pesan = models.IntegerField()
    slug_hewan = models.SlugField()
    slug_toko= models.SlugField()
    st = (
        ('Belum Dibayar', 'Belum Dibayar'),
        ('Pending', 'Pending'),
        ('Konfirmasi', 'Konfirmasi'),
    )
    status_pembelian = models.CharField(max_length=20, choices=st, default="Belum Dibayar")
    
    def save(self):
        self.slug_hewan = slugify(self.nama_hewan)
        self.slug_toko = slugify(self.nama_toko)
        super(pembeli_unconfirm, self).save()
