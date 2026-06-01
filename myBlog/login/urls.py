from django.urls import path
from common.Variables.VariableNames import AuthUrls as URL



from .views import (
    RegisterUser,
    LoginUser,
    LogoutUser,
    ActivateView,
    ForgotPassword,
    ResetPasswordView,
)



urlpatterns = [
    path(URL.Register.register_subUrl, RegisterUser.as_view(), name=URL.Register.register_reverseName),
    path(URL.Login.login_subUrl, LoginUser.as_view(), name=URL.Login.login_reverseName),
    path(URL.Logout.logout_subUrl, LogoutUser.as_view(), name=URL.Logout.logout_reverseName),
    path(URL.UserActivation.activate_subUrl, ActivateView.as_view(), name=URL.UserActivation.activate_reverseName),
    path(URL.ForgotPassword.forgot_password_subUrl, ForgotPassword.as_view(), name=URL.ForgotPassword.forgot_password_reverseName),
    path(URL.PasswordReset.reset_password_subUrl, ResetPasswordView.as_view(), name=URL.PasswordReset.reset_password_reverseName),


]