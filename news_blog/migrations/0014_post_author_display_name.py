# Generated by Django 4.0.5 on 2022-06-24 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_blog', '0013_rename_type_applicationnotification_notification_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_display_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
