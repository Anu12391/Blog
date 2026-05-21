from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from login.models import NewUser

from login.services.authentication_logic.tokens import account_activation_token


def createNewUser(cleaned_data):
    data = cleaned_data.copy()
    data.pop('confirm_password', None)

    return NewUser.objects.create_user(**data)

def isEmailRegistered(email):
    doesExist=NewUser.objects.filter(email=email).exists()
    return doesExist


def getUserByUserId(userId):
    return NewUser.objects.get(id=userId)


def getUId(user):
    return urlsafe_base64_encode(force_bytes(user.pk))

def getUser(userId):
    return getUserByUserId(userId)

def getToken(user):
    return account_activation_token.make_token(user)


def getUserIdFromEmail(email):
    user= NewUser.objects.get(email=email)
    userId=user.id
    return userId

