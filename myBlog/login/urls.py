from django.urls import path

from login.views import register_new_user

urlpatterns = [
    path('', register_new_user, name='register_new_user'),
]