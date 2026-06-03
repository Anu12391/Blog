from django.forms import ModelForm

from login import models
from myProfile.models.UserProfile import EditProfile


class EditProfileForm(ModelForm):
    class Meta:
        model=EditProfile
        fields=('user','birthDate','about')
