from django.shortcuts import render
from django.views import View


class TopicSelection(View):
    def get(self, request):
        return render(request, 'mySettings/topics_selected.html',{})

    def post(self, request):
        pass
