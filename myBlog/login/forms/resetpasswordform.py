from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class ResetPasswordForm(forms.Form):
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super(ResetPasswordForm, self).clean()
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
