from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.db import models

class NewUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.setpassword(password)
        new_user.save()
        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)







# Create your models here.
class NewUser(AbstractBaseUser):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    first_name = models.CharField(max_length=30,blank=False, null=False)
    last_name = models.CharField(max_length=60,blank=False, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES,default='Male')
    joining_date = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']



    def __str__(self):
        return self.email


