# Generated by Django 4.0.5 on 2022-06-27 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_blog', '0015_alter_applicationnotification_notification_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='author_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL),
        ),
    ]