from django.db import models

from myBlog import settings


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")
    birthDate=models.DateField(null=True,blank=True)
    about=models.TextField(null=True,blank=True)
