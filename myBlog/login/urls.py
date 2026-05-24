from django.urls import path

from login.views.RegisterView import register_new_user


from login.views.LoginViews import login_user, logout_user
from login.views.RegisterView import activate

from login.views.ForgotPasswordView import forgotpassword

from login.views.ResetPasswordView import resetPassword

urlpatterns = [
    path('register/', register_new_user, name='register_new_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    path('forgot_password/', forgotpassword, name='forgot_password'),
    path('reset_password/<str:uidb64>/<str:token>/', resetPassword, name='reset_password'),


]