from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from vendor.models import hewan
from details.models import pembeli_unconfirm
from register.models import UserProfile
from django.db.models import F
def index(request, kode, kodetoko):
    pengguna = request.user
    rinci = hewan.objects.get(slug=kode, slug_toko=kodetoko)
    if request.method == "POST":
        if request.user.is_anonymous:
            return redirect('login:index')
        else:
            cek = UserProfile.objects.filter(user= pengguna, status="buyer")
            if not cek:
                return render(request, 'vendor/IndexVendor.html', {'alert_flag':True})
            else:
                pass
            status_tersedia = rinci.jumlah
            nama_hewan = request.POST['nama_hewan']
            nama_toko = request.POST['nama_toko']
            jumlah = int(request.POST['jumlah'])
            harga_pesan = rinci.harga_hewan
            total  = int(harga_pesan * jumlah)
            if jumlah != 0:
                if status_tersedia >= jumlah:
                    a = pembeli_unconfirm(nama_pembeli=pengguna, nama_hewan=nama_hewan, nama_toko=nama_toko, jumlah_pesan=jumlah, harga_pesan=harga_pesan, total_pesan=total)
                    a.save()
                else:
                    return render(request, 'details/details.html', {'alert_capacity':True, 'value':status_tersedia,})
            else:
                return render(request, 'details/details.html', {'alert_error':True})
            
    context={
        'title':'BukaTernak',
        'rincis':rinci,
    }
    return render(request, 'details/details.html', context)


