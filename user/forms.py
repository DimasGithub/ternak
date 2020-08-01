from django import forms
from django.forms import ModelForm
from user.models import pembeli_confirm
class pembelianForm(ModelForm):
    class Meta:
        model = pembeli_confirm
        fields = ('nama_penerima', 'telp_penerima', 'kota_penerima', 'provinsi_penerima', 'alamat_penerima','upload_pembayaran')
        widgets = {
            'nama_penerima':forms.TextInput(attrs={'class':'form-control','placeholder':'Nama Penerima'}),
            'telp_penerima':forms.TextInput(attrs={'class':'form-control','placeholder':'Nomor Telepon Penerima'}),
            'kota_penerima':forms.TextInput(attrs={'class':'form-control','placeholder':'Kota Penerima'}),
            'provinsi_penerima':forms.TextInput(attrs={'class':'form-control','placeholder':'Provinsi Penerima'}),
            'alamat_penerima':forms.Textarea(attrs={'class':'form-control','placeholder':'Alamat Lengkap'}),
            'upload_pembayaran':forms.FileInput(),
        }
