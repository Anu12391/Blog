from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from myPosts.models import Post


class MyAllPostView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'mySettings/topics_selected.html'

    def get_queryset(self):
        allPosts=Post.objects.filter(user=self.request.user)
        return allPosts

