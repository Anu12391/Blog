from django.contrib import admin

from mySettings.models.TopicsOfInterest import Topics, TopicsSelected


# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topicId','topicName', 'topicDescription', )

    ordering = ('topicName',)


class TopicSelectedAdmin(admin.ModelAdmin):
    list_display = ('topic__topicId','topic__topicName', 'user__email')

    ordering = ('topic__topicId',)

admin.site.register(Topics,TopicAdmin)
admin.site.register(TopicsSelected,TopicSelectedAdmin)


