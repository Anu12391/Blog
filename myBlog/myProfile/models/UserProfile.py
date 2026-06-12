import os

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from myBlog import settings


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")
    birthDate=models.DateField(null=True,blank=True)
    about=models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(
        upload_to="profile_pics/",
        null=True,
        blank=True
    )


@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem when corresponding object is updated
    with a new file or cleared.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).profile_pic
    except sender.DoesNotExist:
        return False

    new_file = instance.profile_pic

    # If the file has changed, or been cleared (new_file is empty/False)
    if not old_file == new_file:
        if old_file and os.path.isfile(old_file.path):
            os.remove(old_file.path)
