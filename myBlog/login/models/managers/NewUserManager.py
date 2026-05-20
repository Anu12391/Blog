from django.contrib.auth.base_user import  BaseUserManager




class NewUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):

        if not email:
            raise ValueError('Users must have an email address')

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        print(f" before DEBUG: Manager is processing email: {email}")
        email = self.normalize_email(email)
        print(f" after DEBUG: Manager is processing email: {email}")
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