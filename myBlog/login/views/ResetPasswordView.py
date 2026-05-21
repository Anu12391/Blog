from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.cache import never_cache

from login.services.authentication_logic.user_utils import getUser


@never_cache
def resetPassword(request, uidb64, token):

    try:

        uid = urlsafe_base64_decode(uidb64).decode()

        user = getUser(uid)

    except:
        user = None

    if user and default_token_generator.check_token(user, token):

        if request.method == "POST":

            password = request.POST.get("password")

            user.set_password(password)

            user.save()

            return redirect("login")

        return render(request, "login/reset_password_email.html")

    return render(request, "login/invalid_link.html")

