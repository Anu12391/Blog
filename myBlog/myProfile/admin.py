from django.contrib import admin

from myProfile.models.TopicsOfInterest import Topics
from myProfile.models.UserProfile import Profile

# Register your models here.
admin.site.register(Profile)
admin  .site.register(Topics)