from django import forms
from django.core.exceptions import ValidationError

from login.backends.LoginHelpers import PasswordValidationMixin


class MyCustomPasswordChangeForm(PasswordValidationMixin,forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter current password'}),
        label="Current Password"
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}),
        label="New Password",
        min_length=8  # Custom validation rule
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}),
        label="Confirm New Password"
    )

    def __init__(self, *args, **kwargs):
        # We pass the logged-in user instance into the form initialization
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_current_password(self):
        """ Manually verify the old password against the database """
        current_password = self.cleaned_data.get('current_password')
        if self.user and self.user.is_authenticated:
            if self.user and not self.user.check_password(current_password):
                raise ValidationError("Your current password is incorrect.")
        else:
            raise ValidationError("You must be logged in to change your password.")
        return current_password

    def clean(self):

        cleaned_data = super().clean()


        self.validate_password_strength_and_match()



        return cleaned_data