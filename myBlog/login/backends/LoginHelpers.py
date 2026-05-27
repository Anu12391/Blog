from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class PasswordValidationMixin:

    def validate_password_strength_and_match(self):

        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password:
            try:
                # Django's built-in complexity validator
                validate_password(password)
            except ValidationError as e:
                self.add_error('password', e)

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")


