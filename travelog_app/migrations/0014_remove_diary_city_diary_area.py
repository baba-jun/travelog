# Generated by Django 4.1.13 on 2024-05-22 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelog_app', '0013_alter_areas_prefecture_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='city',
        ),
        migrations.AddField(
            model_name='diary',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='travelog_app.areas', verbose_name='エリア'),
        ),
    ]