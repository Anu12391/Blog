from django.urls import path

from common.Constants.ApplicationNames import AppNames
from common.Constants.VariableNames import AuthUrls
from mySettings.views.TopicSelectionView import TopicSelection


app_name = AppNames.MySettings.app_name

urlpatterns = [
    path(AuthUrls.MyTopics.myTopics_subUrl,TopicSelection.as_view(),name=AuthUrls.MyTopics.myTopics_reverseName)
]