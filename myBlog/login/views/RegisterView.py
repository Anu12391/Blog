from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache

from login.forms.register import RegisterForm
from login.services.signals.EmailLinks.UserActivationEmail import sendActivationEmail
from myBlog import settings


@method_decorator(never_cache, name='dispatch')
class RegisterUser(View):
    def get(self, request):
        reg_form = RegisterForm()
        return render(request, 'login/new_user.html', {'reg_form': reg_form})


    def post(self, request):
        print(request.POST)
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            print(reg_form.cleaned_data)
            user = reg_form.save()

            transaction.on_commit(

                lambda: sendActivationEmail.delay(user.id)
            )
            return redirect("home")
        return render(request, 'login/new_user.html', {'reg_form': reg_form})


















