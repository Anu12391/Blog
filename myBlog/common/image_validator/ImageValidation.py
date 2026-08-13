from django.core.exceptions import ValidationError
from PIL import Image

def validate_image_dimensions(image):
    img = Image.open(image)
    width, height = img.size

    if width > 1920 or height > 1080:
        raise ValidationError(
                "Image dimensions must not exceed 1920x1080 pixels."
        )