from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from vendor.forms import BukaTokoForm, HewanForm
from django.contrib.auth.models import User
from vendor.models import hewan, tokoternak
from django.contrib.auth import logout
from register.models import UserProfile
from user.models import pembeli_confirm
from details.models import pembeli_unconfirm
from django.core.exceptions import ObjectDoesNotExist
from docx import *
import datetime
from docx.shared import Inches
import os
from django.conf import settings
from django.http import HttpResponse, Http404
@login_required
def IndexVendor(request):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="vendor")
    print(cek)
    if not cek:
        return redirect('user:IndexUser')
    else:
        pass
    context = {
        'title':'BukaTernak',
        'header':'Selamat datang',
    }
    return render(request, 'vendor/IndexVendor.html', context)
@login_required
def IndexBukaToko(request):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="vendor")
    print(cek)
    if not cek:
        return redirect('user:IndexUser')
    else:
        pass
    form = BukaTokoForm(request.POST)
    user = request.user
    print(user)
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('vendor:IndexVendor')
        else:
            print('buka toko data tidak valid')
    context={
        'title':'buka toko | bukaternak',
        'forms':form,
    }
    return render(request, 'vendor/IndexBukaToko.html', context)
@login_required
def posting(request):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="vendor")
    if tokoternak.objects.get(user=pengguna):
        try:
            cek_punyatoko = tokoternak.objects.get(user= pengguna)
        except cek_punyatoko.ObjectDoesNotExist:
            cek_punyatoko = None
    else:
        cek_punyatoko = None

    print(cek_punyatoko)
    print(cek)
    if not cek:
        return redirect('user:IndexUser')
    else:
        pass
    user = request.user
    form = HewanForm(request.POST, request.FILES)
    toko = tokoternak.objects.get(user=user)
    print(user)
    print(toko)
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.nama_toko = toko
            form.save()
            return redirect('vendor:IndexVendor')
        else:
            print('posting data tidak valid')
    context={
        'title':'buka toko | bukaternak',
        'forms':form,
    }
    return render(request, 'vendor/Posting.html', context)
@login_required
def ManagePosting(request):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="vendor")
    print(cek)
    if not cek:
        return redirect('user:IndexUser')
    else:
        pass
    user = request.user
    toko = tokoternak.objects.get(user=user)
    form = hewan.objects.filter(nama_toko=toko)
    context={
        'title':'Manage Posting',
        'forms':form,
    }
    return render(request, 'vendor/managePosting.html', context)
@login_required
def ManageDelete(request, kode):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="vendor")
    print(cek)
    if not cek:
        return redirect('user:IndexUser')
    else:
        pass
    form = hewan.objects.filter(id=kode).delete()
    return redirect('vendor:ManagePosting')
@login_required
def ManagePembeli(request):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="vendor")
    print(cek)
    if not cek:
        return redirect('user:IndexUser')
    else:
        pass
    pengguna = request.user.tokoternak.nama_toko
    table = pembeli_confirm.objects.filter(toko= pengguna)
    context={
        'title':'Manage Pembeli | Bukaternak',
        'list' : table,
    }
    return render(request, 'vendor/ManagePembeli.html', context)
def keluar(request):
    logout(request)
    return redirect('index')

@login_required
def konfirmasi(request, kode):
    kode = kode
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="vendor")
    print(cek)
    if not cek:
        return redirect('user:IndexUser')
    else:
        pass
    ubah_status=pembeli_unconfirm.objects.get(kode = kode)
    ubah_status.status_pembelian = "Konfirmasi"
    ubah_status.save()
    cek = pembeli_confirm.objects.get(kodein = kode)
    cek.delete()
    angka = ubah_status.jumlah_pesan
    nama_hewan = ubah_status.nama_hewan
    nama_toko = ubah_status.nama_toko
    ubah_angka= hewan.objects.get(nama_toko=nama_toko, nama_hewan=nama_hewan)
    a = ubah_angka.jumlah
    pri = a-angka
    ubah_angka.jumlah = pri
    ubah_angka.save()
    return redirect('vendor:ManagePembeli')
@login_required
def EditPosting (request, kode):
    pengguna = request.user
    edit_posting = hewan.objects.get(id=kode)
    dataposting = {
        'nama_hewan':edit_posting.nama_hewan,
        'tinggi_hewan':edit_posting.tinggi_hewan,
        'berat_hewan':edit_posting.berat_hewan,
        'harga_hewan':edit_posting.harga_hewan,
        'jumlah': edit_posting.jumlah,
        'kategori': edit_posting.kategori,
        'deskripsi_hewan': edit_posting.deskripsi_hewan,
        'upload_foto':edit_posting.upload_foto,
    }
    form_input = HewanForm(request.POST or None, request.FILES or None, initial=dataposting, instance=edit_posting)
    if request.method == "POST":
        if form_input.is_valid():
            form_input.save()
            return redirect('vendor:IndexVendor')
    context={
        'title':'Edit|Posting',
        'forms':form_input,
    }
    return render(request, 'vendor/Posting.html', context)
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.png")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response   
        raise Http404
# from docx import *
# from docx.shared import Inches

def TestDocument(request, kode):
    data_transaksi = pembeli_confirm.objects.get(id = kode)
    nama_pembeli = data_transaksi.kodein.nama_pembeli
    nama_toko = data_transaksi.kodein.nama_toko
    nama_hewan = data_transaksi.kodein.nama_hewan
    jml_pesan = str(data_transaksi.kodein.jumlah_pesan)
    jml_harga = str(data_transaksi.kodein.total_pesan)
    nama_transaksi = data_transaksi.nama_penerima
    telp_transaksi = data_transaksi.telp_penerima
    provinsi_transaksi = data_transaksi.provinsi_penerima
    kota_transaksi = data_transaksi.kota_penerima
    alamat_transaksi = data_transaksi.alamat_penerima
    kode_transaksi = str(data_transaksi.kodein_id)
    
    document = Document()

    document.add_heading('Bukti Transaksi', 0)

    p = document.add_paragraph('Terima Kasih sudah melakukan pembelian ')
    akun =document.add_paragraph('Akun Pembeli                  : ')
    akun.add_run(nama_pembeli)
    penjual=document.add_paragraph('Toko Penjual                   : ')
    penjual.add_run(nama_toko)

    hewan= document.add_paragraph('Nama Hewan Pesanan    : ')
    hewan.add_run(nama_hewan)
    jmlpesan=document.add_paragraph('Jumlah Pesanan              : ')
    jmlpesan.add_run(jml_pesan)
    jmlharga=document.add_paragraph('Total Biaya Pesanan       : Rp. ')
    jmlharga.add_run(jml_harga)
    jmlharga.add_run(',00 -,')
    document.add_paragraph('==============================================')
    kodetf = document.add_paragraph('Kode Transaksi              : ')
    kodetf.add_run(kode_transaksi)
    nama = document.add_paragraph('Nama Penerima             : ')
    nama.add_run(nama_transaksi)
    telp = document.add_paragraph('Nomor Telepon              : ')
    telp.add_run(telp_transaksi)
    document.add_paragraph('Alamat                           : ')
    addr=document.add_paragraph()
    addr.add_run(alamat_transaksi)
    addr.add_run(',')
    addr.add_run(kota_transaksi)
    addr.add_run(',')
    addr.add_run(provinsi_transaksi)
    document.add_paragraph('==============================================')
    document.add_page_break()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=buktitransaksi.docx'
    document.save(response)
    return response