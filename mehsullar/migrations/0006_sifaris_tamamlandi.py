# Generated by Django 5.1.4 on 2024-12-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0005_remove_sifaris_mehsullar_remove_sifaris_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sifaris',
            name='tamamlandi',
            field=models.BooleanField(default=False),
        ),
    ]
