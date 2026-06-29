from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from mySettings.models import Topics
from mySettings.models.TopicsOfInterest import TopicsSelected
from mySettings.services.settings_utils import getAllToipcs


class TopicSelection(View):
    """Renders the core UI layout frame."""

    def get(self, request, *args, **kwargs):
        currentUser = request.user
        user_selected_topics = TopicsSelected.objects.filter(user=currentUser).values_list('topic__topicId', flat=True)

        context = {
            'allTopics': getAllToipcs(),
            'user_selected_ids': list(user_selected_topics),
        }
        return render(request, 'mySettings/topics_selected.html', context)

    def post(self, request):
        # Your form submission update logic lives cleanly here
        pass


class TopicSearchAPI(View):
    """Dedicated API endpoint for filtering topics. Returns pure JSON."""

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('query', '').strip()

        if search_query:
            topics_pool = Topics.objects.filter(
                Q(topicName__icontains=search_query) |
                Q(topicDescription__icontains=search_query)
            )
        else:
            topics_pool = getAllToipcs()

        # Serialize our model data cleanly into a plain dictionary list
        payload = list(topics_pool.values('topicId', 'topicName'))
        return JsonResponse({'topics': payload}, safe=False)