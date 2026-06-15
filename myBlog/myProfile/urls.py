
from django.urls import path

from common.Constants.ApplicationNames import AppNames
from common.Constants.VariableNames import AuthUrls as URL
from myProfile.views.CustomPasswordChangeDoneView import CustomPasswordChangeDone
from myProfile.views.MyProfileView import MyProfileView
from myProfile.views.PasswordChangedView import ChangePassword

app_name = AppNames.MyProfile.app_name

urlpatterns = [

path(URL.MyProfile.myProfile_subUrl,MyProfileView.as_view(),name=URL.MyProfile.myProfile_reverseName),

path('change_password/',ChangePassword.as_view(),name='change_password'),

path('change-password/done/',CustomPasswordChangeDone.as_view(),name='password_change_done'),

]
