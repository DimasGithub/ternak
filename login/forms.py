from django import forms
class Loginn(forms.Form):
    pengguna = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}), max_length=50)
    sandi = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}), max_length=50)