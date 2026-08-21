from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.Constants.VariableNames import AuthUrls
from myPosts.forms.PostForm import PostForm
from myPosts.models.CreatePostModel import Post


class CreatePostView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    model = Post
    template_name = 'myPosts/create_post.html'
    success_url = reverse_lazy(AuthUrls.Dashboard.dashboard_redirectName)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)





