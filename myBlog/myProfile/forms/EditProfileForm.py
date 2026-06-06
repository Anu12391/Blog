from django import forms

from myProfile.models.UserProfile import Profile


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"readonly": True}),
    )


    class Meta:
        model=Profile
        fields=('email','birthDate','about')



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

        # self.fields['birthDate'].input_formats = ['%Y-%m-%d', '%d-%m-%Y']
