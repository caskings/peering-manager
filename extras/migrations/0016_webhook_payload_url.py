# Generated by Django 4.2.3 on 2023-07-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("extras", "0015_webhook_contentypes")]

    operations = [
        migrations.AlterField(
            model_name="webhook",
            name="payload_url",
            field=models.CharField(
                help_text="This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.",
                max_length=512,
                verbose_name="URL",
            ),
        )
    ]
