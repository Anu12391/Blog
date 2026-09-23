from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from myPosts.models import Post


class MyAllPostView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'myPosts/all_my_posts.html'
    paginate_by = 10
    context_object_name = 'my_posts'

    def get_queryset(self):
        allPosts=Post.objects.filter(created_by=self.request.user)
        return allPosts

