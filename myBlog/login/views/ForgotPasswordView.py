from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from myBlog import settings
from login.forms.forgotpassword import ForgotPasswordForm
from login.services.authentication_logic.user_utils import getUserIdFromEmail
from login.services.signals.EmailLinks.UserActivationEmail import sendForgotPasswordEmail


@never_cache
def forgotpassword(request):
    if request.method == 'POST':
        forgotPasswordForm = ForgotPasswordForm(request.POST)
        if forgotPasswordForm.is_valid():
            email = forgotPasswordForm.cleaned_data['email']
            user=getUserIdFromEmail(email)
            sendForgotPasswordEmail(user)

            print(email)
            return redirect('login_user')
        else:
            messages.error(request, "Email Doesnt Exist")
    else:

        forgotPasswordForm = ForgotPasswordForm()
    return render(request, 'login/forgot_password.html', {'forgotPasswordForm': forgotPasswordForm})
