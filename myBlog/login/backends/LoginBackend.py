from django.contrib.auth.backends import ModelBackend

from login.models import NewUser

from login.services.authentication_logic.user_utils import getUserFromEmail,getUserFromUserId


class LoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=getUserFromEmail(username)

        except NewUser.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None


    def get_user(self, user_id):
        try:
            return getUserFromUserId(user_id)

        except NewUser.DoesNotExist:
            return None