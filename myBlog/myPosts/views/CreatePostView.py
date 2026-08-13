from django.views.generic import CreateView

from myPosts.forms.PostForm import PostForm
from myPosts.models.CreatePostModel import Post


class CreatePostView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'myPosts/create_post.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



