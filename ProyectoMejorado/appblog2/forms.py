from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    last_login = forms.CharField(max_length=100)
    date_joined = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 
        'last_login','date_joined', 'password')

class PasswordChangingForm(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password ', 'new_password1', 'new_password2')