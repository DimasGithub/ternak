from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from register.models import UserProfile
class ExtendedUserCreationForm(UserCreationForm):
    email =  forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name', 'password1','password2')
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email',}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name',}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name',}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password',}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Confirmation'}),
        }
        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob','jenis_kelamin', 'ponsel','status', 'avatar')
        widgets ={
            'dob':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'jenis_kelamin':forms.Select(attrs={'class':'form-control'}),
            'ponsel':forms.TextInput(attrs={'class':'form-control','placeholder':'Ponsel'}),
            'status':forms.Select(attrs={'class':'form-control',}),
            'avatar':forms.FileInput(),
        }