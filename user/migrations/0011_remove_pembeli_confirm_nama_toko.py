# Generated by Django 3.0.7 on 2020-07-13 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200713_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembeli_confirm',
            name='nama_toko',
        ),
    ]
