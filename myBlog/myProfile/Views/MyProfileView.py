from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from common.user_utils import getUserData
from myProfile.forms.EditProfileForm import EditProfileForm


class MyProfileView(LoginRequiredMixin,View):
    def get(self, request):

        userPK=request.user.pk

        userData=getUserData(userPK)

        editProfileForm=EditProfileForm(instance=userData)

        context = {'userData':userData,'editProfileForm':editProfileForm}

        return render(request, 'myProfile/my_profile.html',context)


    def post(self, request):
        pass