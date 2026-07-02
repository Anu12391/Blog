from django.db.models import Q
from django.shortcuts import render
from django.views import View

from mySettings.models import Topics
from mySettings.models.TopicsOfInterest import TopicsSelected
from mySettings.services.settings_utils import getAllToipcs


class TopicSelection(View):


    def get(self, request, *args, **kwargs):
        currentUser = request.user
        user_selected_topics = TopicsSelected.objects.filter(user=currentUser).values_list('topic__topicId', flat=True)
        print(user_selected_topics)
        context = {
            'allTopics': getAllToipcs(),
            'user_selected_ids': list(user_selected_topics),
        }
        return render(request, 'mySettings/topics_selected.html', context)

    def post(self, request):

        pass


class TopicSearchAPI(View):


    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('query', '').strip()

        if search_query:
            topics_pool = Topics.objects.filter(
                Q(topicName__icontains=search_query) |
                Q(topicDescription__icontains=search_query)
            )
        else:
            topics_pool = getAllToipcs()


        print("search api")
        return render(request, 'mySettings/topics_searched.html', {'allTopics': topics_pool})


    class TopicSelectionUpdate(View):
        def post(self, request, *args, **kwargs):
            pass