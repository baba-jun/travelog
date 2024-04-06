# Generated by Django 4.1.13 on 2024-04-06 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelog_app', '0003_remove_diary_post_images_diary_post_image1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='prefectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefecture_id', models.CharField(max_length=2, verbose_name='都道府県コード')),
                ('prefecture_name', models.CharField(max_length=4, verbose_name='都道府県名')),
            ],
            options={
                'verbose_name_plural': 'prefectures',
            },
        ),
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.CharField(max_length=5, verbose_name='市区町村コード')),
                ('city_name', models.CharField(max_length=10, verbose_name='市区町村名')),
                ('prefecture_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelog_app.prefectures', verbose_name='User_ID')),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
