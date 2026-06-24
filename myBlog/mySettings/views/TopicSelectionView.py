from django.db.models import Q
from django.shortcuts import render
from django.views import View

from mySettings.models import Topics
from mySettings.models.TopicsOfInterest import TopicsSelected
from mySettings.services.settings_utils import getAllToipcs


class TopicSelection(View):
    def get(self, request, *args, **kwargs):
        search_query=request.GET.get('query', '').strip()
        if search_query:
            topics_pool = Topics.objects.filter(
                Q(topicName__icontains=search_query) |
                Q(topicDescription__icontains=search_query)
            )
        else:
            topics_pool=getAllToipcs()

        currentUser=request.user
        print(topics_pool)

        user_selected_topics=TopicsSelected.objects.filter(user=currentUser).values_list('topic__topicId', flat=True)

        context = {
            'allTopics': topics_pool,
            'user_selected_ids': list(user_selected_topics),
            'search_query': search_query
        }
        return render(request, 'mySettings/topics_selected.html',context)

    def post(self, request):
        pass
