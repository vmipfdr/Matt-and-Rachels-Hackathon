from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first', 'last', 'email')
        widgets = {
            'first': forms.TextInput(attrs={'placeholder': 'John'}),
            'last': forms.TextInput(attrs={'placeholder': 'Doe'}),
            'email': forms.TextInput(attrs={
                'placeholder': 'youremail@here.com'
            }),
        }
