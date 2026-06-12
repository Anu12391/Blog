from django.contrib import admin

from myProfile.models.TopicsOfInterest import Topics
from myProfile.models.UserProfile import Profile



class TopicAdmin(admin.ModelAdmin):
    list_display = ('topicId','topicName', 'topicDescription', )

    ordering = ('topicId',)


# Register your models here.
admin.site.register(Profile)
admin  .site.register(Topics,TopicAdmin)