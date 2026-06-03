from django.forms import ModelForm

from myProfile.models.UserProfile import Profile


class EditProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=('birthDate','about')
