from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from login.forms.forgotpassword import ForgotPasswordForm
from login.forms.login import LoginForm
from login.forms.register import RegisterForm
from login.models import NewUser
from login.services.authentication_logic.tokens import account_activation_token
from login.services.signals.EmailLinks.UserActivationEmail import sendActivationEmail

from myBlog import settings


@never_cache
def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user=authenticate(request,username=email,password=password)



            if user is not None:
                print("Inside")
                login(request, user)

                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")



    else:
        login_form=LoginForm()
    return render(request, 'login/login.html',{'login_form':login_form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')
