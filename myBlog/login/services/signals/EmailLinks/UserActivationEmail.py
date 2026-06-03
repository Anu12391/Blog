from celery import shared_task
from common.user_utils import getUserByUserId, getUId, getToken
from login.services.signals.EmailLinks.SendEmail import sendEmailContent

from myBlog import settings


@shared_task
def sendActivationEmail(userId):
    user=getUserByUserId(userId)
    token=getToken(user)
    uid=getUId(user)

    subLink = f"user/activate/{uid}/{token}/"
    mail_subject = "Activate your account."
    htmlLink='login/activation_email.html'


    sendEmailContent(user,subLink,mail_subject,htmlLink)


@shared_task
def sendForgotPasswordEmail(userId):
    user = getUserByUserId(userId)
    token = getToken(user)
    uid = getUId(user)
    print("send token",token)
    print("send user",user)

    subLink = f"user/reset_password/{uid}/{token}/"
    mail_subject = "Reset Your Password"
    htmlLink = 'login/reset_password_email.html'

    print("sender", user.pk)
    print("sender", user.password)
    print("sender", type(user))

    sendEmailContent(user, subLink, mail_subject, htmlLink)














