from django.urls import path

from login.views import register_new_user,login_user,logout_user,activate



urlpatterns = [
    path('register/', register_new_user, name='register_new_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),

]