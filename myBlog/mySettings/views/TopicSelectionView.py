from django.shortcuts import render
from django.views import View

from mySettings.services.settings_utils import getAllToipcs


class TopicSelection(View):
    def get(self, request):
        allTopics=getAllToipcs()
        return render(request, 'mySettings/topics_selected.html',{'allTopics':allTopics})

    def post(self, request):
        pass
