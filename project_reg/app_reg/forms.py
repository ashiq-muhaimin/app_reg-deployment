from django import forms
from django.contrib.auth.models import User
from app_reg.models import profileModel

class userForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class profileForm(forms.ModelForm):
    class Meta():
        model = profileModel
        fields = ('portfolio','profile_pic')
