# Generated by Django 3.0.7 on 2020-07-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_hewan_slug_toko'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hewan',
            name='deskripsi_hewan',
            field=models.CharField(max_length=10000),
        ),
    ]
