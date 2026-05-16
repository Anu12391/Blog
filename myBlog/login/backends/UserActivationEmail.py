from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import request
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

from login.backends.tokens import account_activation_token
from myBlog import settings


def sendActivationEmail(user):
    # Build the link components
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    activation_link = f"http://{current_site.domain}/user/activate/{uid}/{token}/"

    # 1. Define the context for the template
    context = {
        'user': user,
        'activation_link': activation_link,
    }

    # 2. Render the HTML content
    html_content = render_to_string('emails/activation_email.html', context)

    # 3. Create a plain-text version for older email clients
    text_content = strip_tags(html_content)

    # 4. Send the email
    send_mail(
        subject=mail_subject,
        message=text_content,  # Plain text version
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_content,  # The magic part that makes it clickable
        fail_silently=False,
    )
