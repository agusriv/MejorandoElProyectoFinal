from django import forms
from appblog.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {

            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
            
        }
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'autor', 'cuerpo', 'descripcion')

        widgets = {

            'titulo': forms.TextInput(attrs={'class' : 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class' : 'form-control'}),
            'autor': forms.Select(attrs={'class' : 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class' : 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class' : 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'cuerpo', 'descripcion')

        widgets = {

            'titulo': forms.TextInput(attrs={'class' : 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class' : 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class' : 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class' : 'form-control'}),

        }