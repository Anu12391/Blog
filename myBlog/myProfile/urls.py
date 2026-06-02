from django.urls import path

from common.Constants.ApplicationNames import AppNames
from common.Constants.VariableNames import AuthUrls as URL
from myProfile.Views.MyProfileView import MyProfileView

app_name = AppNames.MyProfile

urlpatterns = [


path(
        URL.MyProfile.myProfile_subUrl,
        MyProfileView.as_view(),
        name=URL.MyProfile.myProfile_reverseName
    ),


]