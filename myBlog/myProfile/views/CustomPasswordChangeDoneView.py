from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomPasswordChangeDone(LoginRequiredMixin, TemplateView):
    template_name = 'myProfile/password_change_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can pass completely custom variables to your success page here
        context['page_title'] = "Password Changed!"
        return context