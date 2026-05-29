from django.urls import path

from .Variables.VariableNames import register_subUrl, register_reverseName, login_subUrl, login_reverseName, \
    logout_subUrl, logout_reverseName, activate_subUrl, activate_reverseName, forgot_password_subUrl, \
    forgot_password_reverseName, reset_password_subUrl, reset_password_reverseName

from .views import (
    RegisterUser,
    LoginUser,
    LogoutUser,
    ActivateView,
    ForgotPassword,
    ResetPasswordView,
)



urlpatterns = [
    path(register_subUrl, RegisterUser.as_view(), name=register_reverseName),
    path(login_subUrl, LoginUser.as_view(), name=login_reverseName),
    path(logout_subUrl, LogoutUser.as_view(), name=logout_reverseName),
    path(activate_subUrl, ActivateView.as_view(), name=activate_reverseName),
    path(forgot_password_subUrl, ForgotPassword.as_view(), name=forgot_password_reverseName),
    path(reset_password_subUrl, ResetPasswordView.as_view(), name=reset_password_reverseName),


]