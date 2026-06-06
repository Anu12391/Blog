from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from common.Constants.VariableNames import AuthUrls
from common.user_utils import getUserData
from myProfile.forms.EditProfileForm import EditProfileForm


class MyProfileView(LoginRequiredMixin,View):
    def get(self, request):

        userPK=request.user.pk

        profile_instance=getUserData(userPK)
        print(profile_instance.user.email)
        print(profile_instance.about)
        print(profile_instance.birthDate)



        editProfileForm = EditProfileForm(instance=profile_instance)

        context = {'profileData':profile_instance,'editProfileForm':editProfileForm}

        return render(request, 'myProfile/my_profile.html',context)


    def post(self, request):
        userPK = request.user.pk
        profile_instance = getUserData(userPK)

        editProfileForm=EditProfileForm(request.POST,instance=profile_instance)
        context = {'profileData': profile_instance, 'editProfileForm': editProfileForm}

        if editProfileForm.is_valid():
            editProfileForm.save()
            return redirect(AuthUrls.Dashboard.dashboard_redirectName)

        return render(request, 'myProfile/my_profile.html',context)