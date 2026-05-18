import email

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from login.models import NewUser

from common.user_utils import createNewUser

from login.backends.UserAuthentication import isEmailRegistered


class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput()
    )
    class Meta:
        model = NewUser
        fields = ['email', 'first_name', 'last_name', 'gender', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NewUser.objects.filter(email=email).exists():
            self.add_error('email','email is already registered')
        return email

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:

            try:
                validate_password(password)
            except ValidationError as e:
                self.add_error('password', e)

            if password != confirm_password:
                self.add_error('confirm_password', "Passwords do not match")


        return cleaned_data





    def save(self, commit=True):
        return createNewUser(self.cleaned_data)



class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput()

    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput()

    )
    def clean_email(self):
        print("in forgot password form")
        email = self.cleaned_data.get('email')
        isExist=isEmailRegistered(email)
        if not isExist:
            self.add_error('email','email is not registered yet!')
        return email








