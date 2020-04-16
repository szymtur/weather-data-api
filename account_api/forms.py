from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from account_api.validators import username_validator, email_validator, password_validator


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128, label='', widget=forms.TextInput())
    email = forms.CharField(max_length=254, label='', widget=forms.EmailInput())
    pass_first = forms.CharField(max_length=32, label='', widget=forms.PasswordInput())
    pass_second = forms.CharField(max_length=32, label='', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'email address'})
        self.fields['pass_first'].widget.attrs.update({'placeholder': 'password'})
        self.fields['pass_second'].widget.attrs.update({'placeholder': 'password confirmation'})

    def clean(self):
        # username validation
        username = self.cleaned_data.get('username')

        if not username:
            raise ValidationError('username field can not be empty')
        else:
            username_validator(username.lower())

        if User.objects.filter(username=username.lower()).exists():
            raise ValidationError('user account already exists')

        # email address validation
        email_address = self.cleaned_data.get('email')

        if not email_address:
            raise ValidationError('email field can not be empty')
        else:
            email_validator(email_address.lower())

        if User.objects.filter(email=email_address.lower()).exists():
            raise ValidationError('email address already exists')

        # password validation
        if not self.cleaned_data.get('pass_first'):
            raise ValidationError('password field can not be empty')
        elif self.cleaned_data.get('pass_first') != self.cleaned_data.get('pass_second'):
            raise ValidationError('password and confirmation password do not match')
        else:
            password_validator(self.cleaned_data['pass_first'])


class LoginForm(forms.Form):
    user_login = forms.CharField(max_length=128, label='', widget=forms.TextInput())
    password = forms.CharField(max_length=32, label='', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_login'].widget.attrs.update({'placeholder': 'username or email address'})
        self.fields['password'].widget.attrs.update({'placeholder': 'password'})

    def clean(self):
        error_message = 'invalid username | email or password'

        # username / email field validation
        user_login = self.cleaned_data.get('user_login')
        if not user_login:
            raise ValidationError('username field can not be empty')

        user_login = user_login.lower()

        if user_login.count('@'):
            try:
                user_login = User.objects.get(email=user_login).username
            except Exception:
                raise ValidationError(error_message)

        # password field validation
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('password field can not be empty')

        # authenticate user
        user = authenticate(username=user_login, password=password)
        if user:
            self.cleaned_data['user_object'] = user
        else:
            raise ValidationError(error_message)


class RemoveConfirmForm(forms.Form):
    password = forms.CharField(max_length=32, label='', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['placeholder'] = 'password'

    is_correct_flag = False

    # method calls form RemoveUserView class
    def set_is_correct_flag(self):
        self.is_correct_flag = True

    def clean(self):
        if not self.cleaned_data.get('password'):
            raise ValidationError('password field can not be empty')
        if not self.is_correct_flag:
            raise ValidationError('invalid password')
