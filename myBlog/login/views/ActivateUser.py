from django.http import HttpResponse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import View

from login.models import NewUser
from login.services.authentication_logic.tokens import account_activation_token


class ActivateView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = NewUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, NewUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you! Your account is now active. You can login.')
        else:
            return HttpResponse('Activation link is invalid or expired!')