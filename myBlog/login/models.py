from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models




class NewUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):

        if not email:
            raise ValueError('Users must have an email address')

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        email = self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)







# Create your models here.
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




