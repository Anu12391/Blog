from django.db.models.signals import post_save
from django.dispatch import receiver
from login.models import NewUser

from login.services.signals.EmailLinks.UserActivationEmail import sendActivationEmail


@receiver(post_save,sender=NewUser)
def send_email_after_registration(sender, instance, created, **kwargs):
    if created:
        #celery task
        sendActivationEmail.delay(instance.id)
