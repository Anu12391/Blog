from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.cache import never_cache

from login.services.authentication_logic.user_utils import getUserByUId

from login.services.authentication_logic.tokens import account_activation_token


@never_cache
def resetPassword(request, uidb64, token):

    try:
        print("in try")
        uid = force_str(urlsafe_base64_decode(uidb64))
        print(uid)

        user = getUserByUId(uid)
        print("receive",user)
        print("receive",token)

    except:
        print("in catch")
        user = None

    print("receiver",user.pk)
    print("receiver",user.password)
    print("receiver",type(user))

    print(account_activation_token.check_token(user, token))
    if user and account_activation_token.check_token(user, token):

        if request.method == "POST":

            password = request.POST.get("password")

            user.set_password(password)

            user.save()

            return redirect("login")

        return render(request, "login/reset_password_email.html")

    return render(request, "login/invalid_link.html")

