# Generated by Django 4.1.13 on 2024-04-07 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelog_app', '0008_alter_diary_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='travelog_app.cities', verbose_name='市町村区'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='観光地の国'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='prefectures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='travelog_app.prefectures', verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='タイトル'),
        ),
    ]
