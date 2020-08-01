from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm, UserProfileForm
from register.models import UserProfile
from django.contrib.auth.decorators import login_required
def register(request):
    form = ExtendedUserCreationForm(request.POST)
    profile_form = UserProfileForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login:index')
        else:
            print('data tidak valid')
    else:
        print('ini mode get')
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()  
    context={
        'title':'akun|register',
        'forms': form,
        'profile_forms': profile_form,
    }
    return render(request, 'register/regis.html', context)
@login_required
def edituser(request):
    pengguna = request.user
    edit_user = UserProfile.objects.get(user= pengguna)
    datauser ={
        'username':edit_user.user.username,
        'email':edit_user.user.email,
        'first_name':edit_user.user.first_name,
        'last_name':edit_user.user.last_name,
        'dob':edit_user.dob,
        'jenis_kelamin':edit_user.jenis_kelamin,
        'ponsel':edit_user.ponsel,
    }
    form = ExtendedUserCreationForm(request.POST or None, initial=datauser, instance=edit_user)
    profile_form = UserProfileForm(request.POST or None, request.FILES or None, initial=datauser, instance=edit_user)
    if request.method == "POST":
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login:index')
        else:
            print('data tidak valid')
    context={
        'title':'akun|Edit Profile',
        'forms': form,
        'profile_forms': profile_form,
    }
    return render(request, 'register/regis.html', context)