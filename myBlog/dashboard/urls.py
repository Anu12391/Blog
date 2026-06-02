from django.urls import path

from common.Constants.VariableNames import AuthUrls as URL
from dashboard import views

app_name = "dashboard"
urlpatterns = [
   path(URL.Dashboard.dashboard_subUrl, views.homepage, name=URL.Dashboard.dashboard_reverseName),

]

