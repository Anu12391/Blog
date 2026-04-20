from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.db import models

class CustomUserManager(BaseUserManager):







# Create your models here.
class CustomUser(AbstractBaseUser):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    first_name = models.CharField(max_length=30,blank=False, null=False)
    last_name = models.CharField(max_length=60,blank=False, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES,default='Male')

    def __str__(self):
        return self.email


