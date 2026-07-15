from django.db import models

from login.models import NewUser


class Topics(models.Model):
    topicId = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=100)
    topicDescription = models.CharField(max_length=500)





class TopicsSelected(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    selected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents a user from selecting the exact same topic twice
        unique_together = ('user', 'topic')
