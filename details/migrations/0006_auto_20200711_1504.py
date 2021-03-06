# Generated by Django 3.0.7 on 2020-07-11 15:04

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0005_auto_20200711_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembeli_unconfirm',
            name='kode_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.CreateModel(
            name='pembeli_confirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akun_pembeli', models.CharField(max_length=25)),
                ('nama_penerima', models.CharField(max_length=25)),
                ('telp_penerima', models.CharField(max_length=25)),
                ('kota_penerima', models.CharField(max_length=50)),
                ('provinsi_penerima', models.CharField(max_length=50)),
                ('upload_pembayaran', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='avatar/'), upload_to='')),
                ('kode', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='details.pembeli_unconfirm')),
            ],
        ),
    ]
