from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache

from common.Constants.VariableNames import AuthUrls
from login.forms.forgotpassword import ForgotPasswordForm
from common.user_utils import getUserIdFromEmail
from login.services.signals.EmailLinks.UserActivationEmail import sendForgotPasswordEmail
from myBlog import settings


@method_decorator(never_cache, name='dispatch')
class ForgotPassword(View):
    def get(self, request):
        forgotPasswordForm = ForgotPasswordForm()
        return render(request, 'login/forgot_password.html', {'forgotPasswordForm': forgotPasswordForm})

    def post(self, request):
        forgotPasswordForm = ForgotPasswordForm(request.POST)
        if forgotPasswordForm.is_valid():
            email = forgotPasswordForm.cleaned_data['email']
            userId = getUserIdFromEmail(email)
            print("forgot user", userId)
            sendForgotPasswordEmail(userId)

            # return redirect(AuthUrls.Login.login_subUrl)
            return redirect(AuthUrls.Login.login_redirectName)
        else:
            messages.error(request, "Email Doesnt Exist")

        return render(request, 'login/forgot_password.html', {'forgotPasswordForm': forgotPasswordForm})








