from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from vendor.models import hewan, tokoternak
from details.models import pembeli_unconfirm
from register.models import UserProfile
from user.models import pembeli_confirm
from user.forms import pembelianForm
from django.core.paginator import Paginator

@login_required
def IndexUser(request):
    card = hewan.objects.all()
    paginator = Paginator(card, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="buyer")
   
    if not cek:
        return redirect('vendor:IndexVendor')
    else:
        pass
    context = {
        'title':'BukaTernak',
        'header':'Selamat datang',
        'cards':card,
        'page_obj':page_obj,
    }
    return render(request, 'user/IndexUser.html', context)
@login_required
def IndexCheckout(request):
    pengguna = request.user
    list_check = pembeli_unconfirm.objects.filter(nama_pembeli=pengguna, status_pembelian= "Belum Dibayar")
    list_pending = pembeli_unconfirm.objects.filter(nama_pembeli=pengguna, status_pembelian= "Pending")
    list_konfirmasi = pembeli_unconfirm.objects.filter(nama_pembeli=pengguna, status_pembelian= "Konfirmasi")
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="buyer")
    
    if not cek:
        return redirect('vendor:IndexVendor')
    else:
        pass
    context={
        'title':'Checkout|BukaTernak',
        'list':list_check,
        'list2':list_pending,
        'list3':list_konfirmasi,
    }
    return render(request, 'user/checkout.html', context)
@login_required
def ManageDelete(request, kode):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="buyer")
    
    if not cek:
        return redirect('vendor:IndexVendor')
    else:
        pass
    form = pembeli_unconfirm.objects.filter(kode= kode).delete()
    return redirect('user:IndexCheckout')
@login_required
def confirmDelete(request, kode):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="buyer")
    
    if not cek:
        return redirect('vendor:IndexVendor')
    else:
        pass
    form = pembeli_unconfirm.objects.filter(kode= kode).delete()
    return redirect('user:IndexCheckout')
@login_required
def pembelian(request, kode):
    pengguna=request.user
    cek = UserProfile.objects.filter(user= pengguna, status="buyer")
   
    if not cek:
        return redirect('vendor:IndexVendor')
    else:
        pass
    pengguna = request.user
    ubah_status = pembeli_unconfirm.objects.get(nama_pembeli=pengguna, status_pembelian= "Belum Dibayar")
    cek = pembeli_unconfirm.objects.get(nama_pembeli=pengguna, kode=kode)
    form = pembelianForm(request.POST, request.FILES)
    toko = cek.nama_toko
    if request.method == "POST":
        namapenerima = request.POST['namapenerima']
        telppenerima = request.POST['telppenerima']
        kotapenerima = request.POST['kotapenerima']
        provinsipenerima = request.POST['provinsipenerima']
        alamatpenerima = request.POST['alamatpenerima']
        uploadpembayaran = request.FILES['uploadpembayaran']
        ubah_status.status_pembelian = "Pending"
        ubah_status.save()
        data = pembeli_confirm(kodein= cek, nama_penerima= namapenerima, telp_penerima=telppenerima, kota_penerima=kotapenerima, provinsi_penerima=provinsipenerima, alamat_penerima=alamatpenerima, toko= toko, upload_pembayaran= uploadpembayaran)
        data.save()
        return redirect('index')
    else:
        print('get')
    context={
        'title':'Pembelian|BukaTernak',
        'forms':form,
    }
    return render(request, 'user/beli.html', context)
def keluar(request):
    logout(request)
    return redirect('index')
