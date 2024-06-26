# Generated by Django 4.1.13 on 2024-04-21 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelog_app', '0009_alter_diary_city_alter_diary_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='likes',
        ),
        migrations.AddField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.CharField(default=0, max_length=50, verbose_name='タイトル'),
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated_at')),
                ('diary_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelog_app.diary', verbose_name='Diary_ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User_ID')),
            ],
            options={
                'verbose_name_plural': 'likes',
            },
        ),
    ]
