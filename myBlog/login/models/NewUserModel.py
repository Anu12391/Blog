from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models

from login.models.managers.NewUserManager import NewUserManager


class NewUser(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    first_name = models.CharField(max_length=30,blank=False, null=False)
    last_name = models.CharField(max_length=60,blank=False, null=False)
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,default='Male')
    joining_date = models.DateField(auto_now_add=True)
    # is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']



    def __str__(self):
        return self.email