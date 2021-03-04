from django import forms
from django.core import validators


def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError("The Password is too short.")


class SignUp(forms.Form):
    first_name = forms.CharField(initial='First Name', )
    last_name = forms.CharField(required=False)
    email = forms.EmailField(help_text='Enter your email', required=False)
    Address = forms.CharField(required=False, )
    age = forms.IntegerField(required=False, )
    password = forms.CharField(widget=forms.PasswordInput, validators=[check_size, ])
    re_password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_password(self):
        password = self.cleaned_data['Password']
        if len(password) < 4:
            raise forms.ValidationError("Password is too short.")
        return password
