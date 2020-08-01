from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    jk =(
        ('Pria','Pria'),
        ('Wanita','Wanita'),
    )
    jenis_kelamin = models.CharField(max_length=10, choices=jk)
    ponsel = models.CharField(max_length=13)
    st= (
        ('Buyer', 'Buyer'),
        ('Vendor', 'Vendor'),
    )
    status = models.CharField(max_length=10,choices=st)
    fs = FileSystemStorage(location='avatar/')
    avatar = models.FileField(storage=fs, blank=True)
    def __str__(self):
        return self.user.username

# class vendor(models.Model):
#     NamaPelapak = models.CharField(max_length=50)
#     UserPelapak = models.CharField(max_length=50, primary_key=True)
#     PasswordPelapak = models.CharField(max_length=50)
#     TokoPelapak = models.CharField(max_length=50)
#     SloganPelapak = models.CharField(max_length=100)
#     DeskripsiPelapak = models.CharField(max_length=1000)
#     AlamatPelapak = models.CharField(max_length=500)
#     Email = models.EmailField(max_length=50)
#     Ponsel = models.CharField(max_length=13)
    
#     def __str__(self):
#         return "{}".format(self.UserPelapak)
