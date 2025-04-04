from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'autofocus': True,
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введите имя пользователя'}))
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'autocompile': "current-password",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введите ваш пароль'})
    #
    # )


class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
        first_name = forms.CharField()
        last_name = forms.CharField()
        username = forms.CharField()
        email = forms.EmailField()
        password1 = forms.CharField()
        password2 = forms.CharField()
