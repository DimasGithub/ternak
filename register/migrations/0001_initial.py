# Generated by Django 3.0.7 on 2020-07-09 08:07

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('jenis_kelamin', models.CharField(choices=[('Pria', 'Pria'), ('Wanita', 'Wanita')], max_length=10)),
                ('ponsel', models.CharField(max_length=13)),
                ('status', models.CharField(choices=[('Buyer', 'Buyer'), ('Vendor', 'Vendor')], max_length=10)),
                ('avatar', models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='avatar/'), upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
