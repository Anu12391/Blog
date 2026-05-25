from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError




from login.models import NewUser

from login.services.authentication_logic.user_utils import createNewUser

from login.backends.LoginHelpers import PasswordValidationMixin


class RegisterForm(PasswordValidationMixin,forms.ModelForm):

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

        self.validate_password_strength_and_match()




        return cleaned_data





    def save(self, commit=True):
        return createNewUser(self.cleaned_data)
