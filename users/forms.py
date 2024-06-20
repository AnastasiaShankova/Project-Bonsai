from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user_name_login', 'placeholder': 'Введите логин', 'name': 'user'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'pass', 'placeholder': 'Введите пароль', 'name': 'pass'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user_name_registr', 'placeholder': 'Введите имя', 'name': 'user_name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user_surname', 'placeholder': 'Введите фамилию', 'name': 'user_surname'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user_name_registr', 'placeholder': 'Введите логин', 'name': 'user'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'user_email_registr', 'placeholder': 'Введите адрес эл. почты', 'name': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'pass', 'placeholder': 'Введите пароль', 'name': 'password1'}))
    password2 = forms.CharField(initial="rt", widget=forms.PasswordInput(
        attrs={'class': 'pass', 'placeholder': 'Подтвердите пароль', 'name': 'password2'}))

    class Meta:
        model = User
        labels = {'password1': 'Введите пароль',
                  'password2': 'Повторите пароль', }
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user_name', 'name': 'user_name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user_surname', 'name': 'user_surname'}))
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'user_photo'}), required=False)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'user', 'name': 'user', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'user_email', 'name': 'email', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'photo', 'username', 'email')
['Nothing', 'will', 'work', 'unless', 'you', 'do']
