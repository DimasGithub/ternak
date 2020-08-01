from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from vendor.models import tokoternak, hewan
class BukaTokoForm(ModelForm):
    class Meta:
        model = tokoternak
        fields = ('nama_toko','pemilik_toko','email_toko','alamat','kota','provinsi','no_telp','deskripsi_toko')
        widgets={
        'nama_toko':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Toko'}),
        'pemilik_toko':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Pemilik Toko'}),
        'email_toko':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Toko'}),
        'alamat':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Alamat'}),
        'no_telp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomor Telepon'}),
        'kota':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kota'}),
        'provinsi':forms.TextInput(attrs={'class':'form-control', 'placeholder':'provinsi'}),
        'deskripsi_toko':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi Toko'}),
        }
class HewanForm(ModelForm):
    class Meta:
        model = hewan
        fields = ('nama_hewan','tinggi_hewan','berat_hewan','jumlah','harga_hewan','kategori', 'deskripsi_hewan','upload_foto')
        widgets={
        'nama_hewan':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contoh : sapi australia'}),
        'tinggi_hewan':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contoh : 1'}),
        'berat_hewan':forms.TextInput(attrs={'class':'form-control', 'placeholder':'contoh : 1000'}),
        'jumlah':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contoh : 200'}),
        'harga_hewan':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contoh : 22000000'}),
        'kategori':forms.Select(attrs={'class':'form-control',}),
        'deskripsi_hewan':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi Hewan'}),
        'upload_foto':forms.FileInput(),
        }
