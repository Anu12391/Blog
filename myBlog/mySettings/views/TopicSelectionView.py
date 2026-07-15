import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from myProfile.models import Profile
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
        data = json.loads(request.body)
        selected_topic_ids = data.get("selectedTopicIds", [])

        current_ids = set(
            TopicsSelected.objects.filter(user=request.user)
            .values_list("topic_id", flat=True)
        )

        new_ids = set(selected_topic_ids)

        # Remove unchecked topics
        TopicsSelected.objects.filter(
            user=request.user,
            topic_id__in=current_ids - new_ids
        ).delete()

        # Add newly checked topics
        TopicsSelected.objects.bulk_create(
            [
                TopicsSelected(user=request.user, topic_id=topic_id)
                for topic_id in (new_ids - current_ids)
            ],
            ignore_conflicts=True,
        )

        topics = Topics.objects.filter(topicId__in=selected_topic_ids)

        return JsonResponse({
            "success": True,
            "updated_topics": list(
                topics.values("topicId", "topicName")
            ),
        })