from django.contrib import admin

from mySettings.models.TopicsOfInterest import Topics


# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topicId','topicName', 'topicDescription', )

    ordering = ('topicId',)

admin  .site.register(Topics,TopicAdmin)


