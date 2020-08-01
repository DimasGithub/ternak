# Generated by Django 3.0.7 on 2020-07-11 18:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0009_auto_20200711_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembeli_unconfirm',
            name='id',
        ),
        migrations.AlterField(
            model_name='pembeli_unconfirm',
            name='kode',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
