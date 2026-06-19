from django.db.models import Q
from django.shortcuts import render
from django.views import View

from mySettings.models import Topics


class TopicSearchView(View):
    def get(self, request, *args, **kwargs):

        searchQuery = request.GET.get('query')

        searchResults=Topics.objects.filter(
                            Q(topicName__icontains=searchQuery) |
                            Q(topicDescription__icontains=searchQuery)
        )

        context = {
            'allTopics': searchResults,
            'search_query': searchQuery
        }

        return render(request, 'mySettings/topics_selected.html', context)
