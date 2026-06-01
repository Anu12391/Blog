from django.contrib.auth.forms import logger
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.decorators.cache import never_cache

from common.Variables import login_reverseName
from login.forms.resetpasswordform import ResetPasswordForm
from login.services.authentication_logic.tokens import account_activation_token
from login.services.authentication_logic.user_utils import getUserByUId


@method_decorator(never_cache, name='dispatch')
class ResetPasswordView(View):
    template_name = "login/reset_password_email.html"
    invalid_template = "login/invalid_link.html"

    def get_user(self, uidb64):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            return getUserByUId(uid)
        except (TypeError, ValueError, OverflowError):
            return None

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user and account_activation_token.check_token(user, token):
            form = ResetPasswordForm(user)
            return render(request, self.template_name, {"resetPasswordForm": form})

        return render(request, self.invalid_template)

    def post(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user and account_activation_token.check_token(user, token):
            form = ResetPasswordForm(user, request.POST)

            if form.is_valid():
                form.save()
                return redirect(login_reverseName)

            logger.warning(f"Password reset validation failed for user ID {user.pk}.")
            return render(request, self.template_name, {"resetPasswordForm": form})

        return render(request, self.invalid_template)


# @never_cache
# def resetPassword(request, uidb64, token):
#
#     try:
#
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = getUserByUId(uid)
#
#     except:
#
#         user = None
#
#     if user and account_activation_token.check_token(user, token):
#
#         if request.method == "POST":
#             resetPasswordForm = ResetPasswordForm(user, request.POST)
#
#             if resetPasswordForm.is_valid():
#                 resetPasswordForm.save()
#                 return redirect("login_user")
#             else:
#                 logger.warning(f"Password reset validation failed for user ID {user.pk}.")
#
#         else:
#             resetPasswordForm = ResetPasswordForm(user)
#
#         return render(request, "login/reset_password_email.html",{"resetPasswordForm":resetPasswordForm})
#
#     else:
#         return render(request, "login/invalid_link.html")
#
#
