# Generated by Django 3.0.7 on 2020-07-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='harga_hewan',
        ),
        migrations.AlterField(
            model_name='checkout',
            name='jumlah_pesan',
            field=models.IntegerField(),
        ),
    ]
