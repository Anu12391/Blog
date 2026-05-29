from django.urls import path


from login.views.ActivateUser import ActivateView
from login.views.ForgotPasswordView import ForgotPassword
from login.views.LoginViews import LoginUser, LogoutUser
from login.views.RegisterView import RegisterUser
from login.views.ResetPasswordView import ResetPasswordView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_new_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', LogoutUser.as_view(), name='logout_user'),
    path('activate/<str:uidb64>/<str:token>/', ActivateView.as_view(), name='activate'),
    path('forgot_password/', ForgotPassword.as_view(), name='forgot_password'),
    path('reset_password/<str:uidb64>/<str:token>/', ResetPasswordView.as_view(), name='reset_password'),


]