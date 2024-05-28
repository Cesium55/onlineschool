from .models import Users
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:

        
        model = Users
        fields = ['login', 'password']

        widgets = {
            "login": TextInput(attrs={
                'class': 'form__input form__email__signup',
                'placeholder': 'Email'
            }),
            "password": TextInput(attrs={
                'class': 'form__input form__password__signup',
                'placeholder': 'Пароль',
                'type': 'password'
            })
        }