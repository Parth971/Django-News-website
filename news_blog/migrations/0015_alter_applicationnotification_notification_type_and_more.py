# Generated by Django 4.0.5 on 2022-06-25 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_blog', '0014_post_author_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationnotification',
            name='notification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_blog.notificationtype'),
        ),
        migrations.AlterField(
            model_name='applicationnotification',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_blog.notificationstatus'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_blog.categorie'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_blog.poststatus'),
        ),
        migrations.AlterField(
            model_name='postnotification',
            name='notification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_blog.notificationtype'),
        ),
        migrations.AlterField(
            model_name='postrecycle',
            name='deleted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postrecycle',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_blog.post'),
        ),
    ]
