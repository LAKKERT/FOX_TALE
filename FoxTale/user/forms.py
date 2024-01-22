from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .models import UserProfileModel
from django.forms import ModelForm, TextInput, Select, Textarea, CharField, EmailField, PasswordInput, IntegerField, ChoiceField

class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email_field',
        'type': 'email',
        'placeholder': 'Enter email here',
        'spellcheck': 'false',
        'name': 'email',
        'id': 'email',
    }))

    month = forms.CharField(widget=forms.Select(attrs={
        'id': 'select_month',
        'placeholde': 'month',
        'class': 'custom_select',
    }))

    day = forms.IntegerField(widget=forms.Select(attrs={
        'id': 'select_day',
        'placeholder': 'day',
        'class': 'custom_select_day',
    }))

    year = forms.IntegerField(widget=forms.Select(attrs={
        'id': 'select_year',
        'placeholder': 'year',
        'class': 'custom_select_year',
    }))

    username = CharField(widget=forms.TextInput(attrs={
        'class': 'user_field',
        'placeholder': 'USERNAME',
        'spellcheck': 'false',
        'id': 'username_id',
        'name': 'username',
        'type': 'text',
    }))

    password1 = CharField(widget=forms.PasswordInput(attrs={
        'class': 'user_field',
        'placeholder': 'PASSWORD',
        'id': 'password1_id',
        'name': 'password1',
        'type': 'password',
    }))

    password2 = CharField(widget=forms.PasswordInput(attrs={
        'class': 'user_field',
        'placeholder': 'CONFIRM PASSWORD',
        'id': 'password2_id',
        'name': 'password1',
        'type': 'password',

    }))

    class Meta:
        model = User
        fields = [
            'email',
            'month',
            'day',
            'year',
            'username',
            'password1',
            'password2',
        ]

class UserLoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={
        'class': 'field',
        'type': 'text',
        'placeholder': 'LOGIN',
        'spellcheck': 'false',
        'autocomplete': 'off',
    }))

    password = CharField(widget=PasswordInput(attrs={
        'class': 'field',
        'placeholder': 'PASSWORD',
        'spellcheck': 'false',
        'autocomplete': 'off',
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class ChangePasswordForm(forms.Form):
    old_password = CharField(widget=PasswordInput(attrs={
        'class': 'password_field',
        'placeholder': 'OLD PASSWORD',
        'type': 'password',
        'spellcheck': 'false',
        'autocomplete': 'off',
    }))

    new_password1 = CharField(widget=PasswordInput(attrs={
        'class': 'password_field',
        'placeholder': 'NEW PASSWORD',
        'type': 'password',
        'spellcheck': 'false',
        'autocomplete': 'off',
    }))

    new_password2 = CharField(widget=PasswordInput(attrs={
        'class': 'password_field',
        'placeholder': 'REPEAT NEW PASSWORD',
        'type': 'password',
        'spellcheck': 'false',
        'autocomplete': 'off',
    }))

    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]

class UserEmailChangeForm(forms.ModelForm):
    new_email = forms.EmailField(widget=TextInput(attrs={
        'placeholder': 'ENTER YOUR NEW EMAIL',
        'class': 'password_field',
        'type': 'email',
        'spellcheck': 'false',
        'autocomplete': 'off',
    }))

    class Meta:
        model = User
        fields = [
            'new_email'
        ]   