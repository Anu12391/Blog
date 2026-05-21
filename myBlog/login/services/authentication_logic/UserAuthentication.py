from django.contrib.auth import authenticate

from login.models import NewUser


def authenticate_user(username, password):

    user = authenticate(username=username, password=password)

    if user is None:
        return None, "Invalid username or password"

    if not user.is_active:
        return None, "Your account is not activated. Please verify your email."

    return user, None



