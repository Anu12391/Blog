
from django.urls import path
from django.views.generic import TemplateView

from common.Constants.ApplicationNames import AppNames
from common.Constants.VariableNames import AuthUrls as URL
from myProfile.Views.CustomPasswordChangeView import CustomPasswordChange

from myProfile.Views.MyProfileView import MyProfileView

app_name = AppNames.MyProfile.app_name

urlpatterns = [

path(URL.MyProfile.myProfile_subUrl,MyProfileView.as_view(),name=URL.MyProfile.myProfile_reverseName),
path('change-password/', CustomPasswordChange.as_view(), name='password_change'),
    path('change-password/done/',
         TemplateView.as_view(template_name='myProfile/change_password_done.html'),
         name='password_change_done'
    ),

]
