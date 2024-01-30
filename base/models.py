from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Create your models here.
class ContactForm(models.Model):
    first_name = models.CharField(_("First name"), blank=True, max_length=55)
    last_name = models.CharField(_("Last name"), blank=True, max_length=55)
    email = models.CharField(_("Email"), blank=True, max_length=55)
    subject = models.CharField(_("Subject"), blank=True, max_length=55)
    message = models.CharField(_("Message"), blank=True, max_length=500)
    created_at = models.DateTimeField(_("Created at"), default=datetime.now)

    class Meta:
        verbose_name = _("contact form")
        verbose_name_plural = _("contact forms")
