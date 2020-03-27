from django import forms
from .models import Post, Comment


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('first', 'last', 'email')
