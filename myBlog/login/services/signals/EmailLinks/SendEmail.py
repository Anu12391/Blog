from django.conf import settings
from django.contrib.sites.models import Site

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from login.models import NewUser



def sendEmailContent(user,subLink,mail_subject):
    current_site = Site.objects.get_current()

    activation_link = f"http://{current_site.domain}/{subLink}"

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
