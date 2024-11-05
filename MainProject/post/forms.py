from django.forms import  ModelForm
from django import forms
from .models import *
class UserForm(ModelForm):
    confirm_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
class RegisterForm(ModelForm):
    class Meta:
        model = Person
        exclude = 'user'
class LoginForm(ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
