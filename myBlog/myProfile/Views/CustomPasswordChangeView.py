from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin

from myProfile.forms import MyCustomPasswordChangeForm


class CustomPasswordChange(LoginRequiredMixin, FormView):
    template_name = 'myProfile/change_password.html'
    form_class = MyCustomPasswordChangeForm
    success_url = reverse_lazy('myProfile:password_change_done')

    def get_form_kwargs(self):
        """ Pass the logged-in user instance directly into our custom form """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        new_password = form.cleaned_data.get('new_password')

        # 1. HERE IT IS: Explicitly hashing the raw text password
        user.set_password(new_password)

        # 2. Save the updated instance into your database
        user.save()

        # 3. CRITICAL: Keeps the user's session valid using your custom LoginBackend setup
        update_session_auth_hash(self.request, user)

        messages.success(self.request, "Your password has been securely updated!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was a problem updating your password.")
        return super().form_invalid(form)