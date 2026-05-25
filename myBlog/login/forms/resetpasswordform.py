from django import forms

from login.backends.LoginHelpers import PasswordValidationMixin


class ResetPasswordForm(PasswordValidationMixin,forms.Form):
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):

        self.user = user
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ResetPasswordForm, self).clean()
        self.validate_password_strength_and_match()


        return cleaned_data


    def save(self):
        password = self.cleaned_data.get("password")
        print(password)
        print(self.user)
        self.user.set_password(password)
        self.user.save()
        return self.user

