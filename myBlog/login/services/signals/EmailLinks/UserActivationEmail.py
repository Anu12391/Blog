from celery import shared_task
from login.models import NewUser
from login.services.authentication_logic.user_utils import getUserByUserId, getUId, getToken
from login.services.signals.EmailLinks.SendEmail import sendEmailContent

from myBlog import settings


@shared_task
def sendActivationEmail(userId):
    user=getUserByUserId(userId)
    token=getToken(user)
    uid=getUId(user)

    subLink = f"user/activate/{uid}/{token}/"
    mail_subject = "Activate your account."
    htmlLink='emails/activation_email.html'


    sendEmailContent(user,subLink,mail_subject,htmlLink)


@shared_task
def sendForgotPasswordEmail(userId):
    user = getUserByUserId(userId)
    token = getToken(user)
    uid = getUId(user)

    subLink = f"user/reset_password/{uid}/{token}/"
    mail_subject = "Reset Your Password"
    htmlLink = 'emails/reset_password_email.html'

    sendEmailContent(user, subLink, mail_subject, htmlLink)







