# Generated by Django 3.0.7 on 2020-07-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_pembeli_confirm_nama_toko'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembeli_confirm',
            name='toko',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
