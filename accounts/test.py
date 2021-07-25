from django.conf import settings
from django.core.mail import send_mail

from_email = getattr(settings, 'DEFAULT_FROM_EMAIL')
sent = send_mail("Hello", "Hello Rick", from_email, ("ochomrichard752@gmail.com", ), fail_silently=False)
if sent == 1:
    print("email sent: "+str(sent))
else:
    print("email not sent")
