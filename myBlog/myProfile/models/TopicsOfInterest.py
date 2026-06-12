from django.db import models


class Topics(models.Model):
    topicId = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=100)
    topicDescription = models.CharField(max_length=500)



