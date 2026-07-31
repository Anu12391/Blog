from django.views.generic import CreateView


class CreatePostView(CreateView):
    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)