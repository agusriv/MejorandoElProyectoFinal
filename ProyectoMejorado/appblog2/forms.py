from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from appblog.models import Perfil


class PerfilPageForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('bio', 'perfil_imagen', 'Instagram_url', 'github_url', 'fb_url', 'web_url', 'Twitter_url')
    
        widgets = {
            'bio': forms.Textarea(attrs={'class' : 'form-control'}),
            #'perfil_imagen': forms.TextInput(attrs={'class' : 'form-control'}),
            'Instagram_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'github_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'fb_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'web_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'Twitter_url': forms.TextInput(attrs={'class' : 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
       

        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 
        'last_login','date_joined', 'password')

class PasswordChangingForm(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('old_password ', 'new_password1', 'new_password2')