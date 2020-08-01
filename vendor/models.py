from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
class tokoternak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_toko = models.CharField(max_length=25, primary_key=True)
    pemilik_toko = models.CharField(max_length=25)
    email_toko = models.EmailField(max_length=25)
    alamat = models.CharField(max_length=100)
    kota = models.CharField(max_length=25, default= "")
    provinsi = models.CharField(max_length=30, default="")
    no_telp = models.CharField(max_length=20)
    deskripsi_toko = models.CharField(max_length=100)
    # def __str__(self):
    #     return "{}({})".format(self.user.username, self.tokoternak.nama_toko)
class hewan(models.Model):
    nama_toko = models.ForeignKey(tokoternak,on_delete=models.CASCADE)
    nama_hewan = models.CharField(max_length=25)
    tinggi_hewan = models.IntegerField(default=0)
    berat_hewan = models.FloatField(default=0)
    harga_hewan = models.IntegerField(default=0)
    jumlah = models.IntegerField(default=0)
    jenishewan=(
        ('Ternak Hewan Unggas', 'Ternak Hewan Unggas'),
        ('Ternak Hewan Kecil', 'Ternak Hewan Kecil'),
        ('Ternak Hewan Besar','Ternak Hewan Besar'),
        ('Ternak Hewan Serangga','Ternak Hewan Serangga'),
        ('Ternak Hewan Vertebrata', 'Ternak Hewan Vertebrata'),
    )
    kategori  = models.CharField(max_length=25, choices=jenishewan)
    deskripsi_hewan = models.CharField(max_length=10000)
    fs = FileSystemStorage(location='avatar/')
    upload_foto = models.FileField(storage=fs)
    slug = models.SlugField()
    slug_toko = models.SlugField()
    def save(self):
        self.slug = slugify(self.nama_hewan)
        self.slug_toko = slugify(self.nama_toko)
        super(hewan, self).save()