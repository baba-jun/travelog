# Generated by Django 4.1.13 on 2024-04-06 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelog_app', '0006_remove_cities_id_alter_cities_city_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='prefecture_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelog_app.prefectures', verbose_name='都道府県コード'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='prefectures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='travelog_app.prefectures', verbose_name='都道府県'),
        ),
    ]
