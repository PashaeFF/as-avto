# Generated by Django 5.1.4 on 2024-12-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0002_sebet'),
    ]

    operations = [
        migrations.AddField(
            model_name='mehsul',
            name='qiymet',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
