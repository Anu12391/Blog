from celery import shared_task
from myBlog import settings
from login.models import NewUser
from login.services.authentication_logic.user_utils import getUserByUserId, getUId, getToken
from login.services.signals.EmailLinks.SendEmail import sendEmailContent


@shared_task
def sendActivationEmail(userId):
    user=getUserByUserId(userId)
    token=getToken(user)
    uid=getUId(user)
    activation_link = f"user/activate/{uid}/{token}/"
    mail_subject = "Activate your account."
    sendEmailContent(user,activation_link,mail_subject)

