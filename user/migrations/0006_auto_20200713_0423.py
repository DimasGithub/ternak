# Generated by Django 3.0.7 on 2020-07-13 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200711_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembeli_confirm',
            name='kodein_id',
        ),
        migrations.AddField(
            model_name='pembeli_confirm',
            name='kodein',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
