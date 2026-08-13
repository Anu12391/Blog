import uuid

from django.conf import settings
from django.db import models

from common.image_validator.ImageValidation import validate_image_dimensions


class Post(models.Model):
    post_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    topic = models.ForeignKey(
        "Topics",
        on_delete=models.PROTECT,
        related_name="posts"
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        validators=[validate_image_dimensions]
    )
    title = models.CharField(max_length=200)

    content = models.TextField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


