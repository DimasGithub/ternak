# Generated by Django 3.0.7 on 2020-07-11 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_pembeli_confirm_akun_pembeli'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pembeli_confirm',
            old_name='kode',
            new_name='kodein',
        ),
    ]
