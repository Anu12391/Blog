from django.contrib.auth.forms import logger
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.cache import never_cache

from login.services.authentication_logic.user_utils import getUserByUId

from login.services.authentication_logic.tokens import account_activation_token

from login.forms.resetpasswordform import ResetPasswordForm


@never_cache
def resetPassword(request, uidb64, token):

    try:

        uid = force_str(urlsafe_base64_decode(uidb64))
        user = getUserByUId(uid)

    except:

        user = None

    if user and account_activation_token.check_token(user, token):

        if request.method == "POST":
            resetPasswordForm = ResetPasswordForm(user, request.POST)

            if resetPasswordForm.is_valid():
                resetPasswordForm.save()
                return redirect("login_user")
            else:
                logger.warning(f"Password reset validation failed for user ID {user.pk}.")

        else:
            resetPasswordForm = ResetPasswordForm(user)
            return render(request, "login/reset_password_email.html",{"resetPasswordForm":resetPasswordForm})

    return render(request, "login/invalid_link.html")

