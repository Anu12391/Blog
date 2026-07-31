from dashboard import models
from mySettings.models import Topics


class CreatePost(models.Model):
    topic=models.ForeignKey(Topics,on_delete=models.CASCADE)
    postId = models.CharField(max_length=30, unique=True, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()


