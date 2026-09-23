from django.urls import path

from myPosts.views.CreatePostView import CreatePostView
from myPosts.views.MyPostView import MyAllPostView

urlpatterns = [


    path('addPost/', CreatePostView.as_view(), name='addPost'),
    path('allPosts/', MyAllPostView.as_view(), name="my-post"),
]