from django.contrib.auth.backends import ModelBackend


class LoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        pass

    def get_user(self, user_id):
        pass