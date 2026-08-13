from django.urls import path

from myPosts.views.CreatePostView import CreatePostView

urlpatterns = [


    path('addPost/', CreatePostView.as_view(), name='addPost'),
]