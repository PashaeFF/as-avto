# Generated by Django 5.1.4 on 2024-12-23 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0011_alter_sifaris_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sifaris',
            name='cemi_mebleg',
        ),
    ]
