from celery import shared_task
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from myBlog import settings
from login.models import NewUser
from login.services.authentication_logic.user_utils import getUserByUserId, getUId, getToken
from login.services.signals.EmailLinks.SendEmail import sendEmailContent


@shared_task
def sendActivationEmail(userId):
    user=getUserByUserId(userId)
    token=getToken(user)
    uid=getUId(user)

    subLink = f"user/activate/{uid}/{token}/"
    mail_subject = "Activate your account."


    sendEmailContent(user,subLink,mail_subject)







