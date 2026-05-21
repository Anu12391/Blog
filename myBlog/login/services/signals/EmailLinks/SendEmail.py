from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myBlog import settings
from login.models import NewUser



def sendEmailContent(user,activation_link,mail_subject):
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
