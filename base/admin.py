from django.contrib import admin

from base.models import ContactForm


# Register your models here.
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "subject",
        "email",
        "message",
        "created_at",
    ]
