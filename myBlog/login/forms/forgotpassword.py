from django import forms

from django import forms

from login.services.authentication_logic.user_utils import isEmailRegistered


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
