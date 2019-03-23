from django import forms
from .models import Blog,Users


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'body',
            'image',
            'price',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'username',
            #'password',
        ]