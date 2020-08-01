from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from register.models import UserProfile
from django.contrib.auth.models import User
def IndexLogin(request):
    username = request.POST.get('pengguna')
    password = request.POST.get('sandi')
    if request.method == "POST":
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            test1 = User.objects.get(username=username)
            print(test1)
            if UserProfile.objects.filter(user=test1, status='Buyer').exists():
                print('ada di buyer')
                return redirect('user:IndexUser')
            elif UserProfile.objects.filter(user=test1, status='Vendor').exists():
                print('ada di buyer')
                return redirect('vendor:IndexVendor')
            else:
                return redirect('login:index')
        else:
            print('ga ada user')
            return redirect('login:index')

    context ={
        'title':'Login | BukaTernak',
        'header':'Login',
    }
    return render(request, 'login/IndexLogin.html', context)
