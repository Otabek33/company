# Generated by Django 5.0.1 on 2024-01-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_contactform_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactform",
            name="message",
            field=models.CharField(blank=True, max_length=500, verbose_name="Message"),
        ),
    ]
