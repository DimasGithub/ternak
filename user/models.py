from django.db import models
from details.models import pembeli_unconfirm
from django.core.files.storage import FileSystemStorage
class pembeli_confirm(models.Model):
    kodein = models.OneToOneField(pembeli_unconfirm, on_delete=models.CASCADE)
    nama_penerima = models.CharField(max_length=25)
    telp_penerima = models.CharField(max_length=25)
    kota_penerima = models.CharField(max_length=50)
    provinsi_penerima = models.CharField(max_length=50)
    alamat_penerima = models.CharField(max_length=1000)
    toko = models.CharField(max_length=25)
    fs = FileSystemStorage(location='avatar/')
    upload_pembayaran = models.FileField(storage=fs)