from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Podaj hasło",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło",widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'my-username-class'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'my-password-class'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'my-password-class'}
        )


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Imię", required=False)
    last_name = forms.CharField(label="Nazwisko", required=False)
    ntrp = forms.FloatField(label="Twój poziom gry w skali NTRP", required=False)
    social = forms.CharField(label="Dodatkowe informacje o Tobie, dodaj link do twojego wybranego komunikatora, aby umożliwić komunikację (Facebook, Instagram...)", required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'ntrp', 'social')

class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'my-username-class'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'my-password-class'}
    )