from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from login.forms.register import RegisterForm
from login.services.signals.EmailLinks.UserActivationEmail import sendActivationEmail
from myBlog import settings


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



# # Create your views here.
# @never_cache
# def register_new_user(request):
#      if request.method == 'POST':
#          print(request.POST)
#          reg_form=RegisterForm(request.POST)
#          if reg_form.is_valid():
#              print(reg_form.cleaned_data)
#              user=reg_form.save()
#
#              transaction.on_commit(
#
#                  lambda: sendActivationEmail.delay(user.id)
#              )
#              return redirect("home")
#
#      else:
#         reg_form = RegisterForm()
#      return render(request, 'login/new_user.html',{'reg_form':reg_form})




# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = NewUser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, NewUser.DoesNotExist):
#         user = None
#
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Thank you! Your account is now active. You can login.')
#     else:
#         return HttpResponse('Activation link is invalid or expired!')















