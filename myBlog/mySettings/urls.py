from django.urls import path

from common.Constants.ApplicationNames import AppNames
from common.Constants.VariableNames import AuthUrls

from mySettings.views.TopicSelectionView import TopicSelection, TopicSearchAPI,TopicSelectionUpdate

app_name = AppNames.MySettings.app_name

urlpatterns = [
    path(AuthUrls.MyTopics.myTopics_subUrl,TopicSelection.as_view(),name=AuthUrls.MyTopics.myTopics_reverseName),
    path(AuthUrls.MyTopics.myTopics_subUrl, TopicSelection.as_view(), name=AuthUrls.MyTopics.myTopics_reverseName),
    path('topics/search/', TopicSearchAPI.as_view(), name='api_topic_search'),
    path('topics/update/', TopicSelectionUpdate.as_view(), name='updateSelectedTopics'),
]