from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache

from login.forms.login import LoginForm
from myBlog import settings
from common.Constants.VariableNames import AuthUrls


@method_decorator(never_cache, name='dispatch')
class LoginUser(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login/login.html', {'login_form': login_form})

    def post(self, request):

        print(request.POST)
        login_form = LoginForm(request.POST)

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

        return render(request, 'login/login.html', {'login_form': login_form})



class LogoutUser(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect(AuthUrls.Login.login_redirectName)










