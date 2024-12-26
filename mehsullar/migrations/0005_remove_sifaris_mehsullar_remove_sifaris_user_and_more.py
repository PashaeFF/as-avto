# Generated by Django 5.1.4 on 2024-12-23 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehsullar', '0004_sifaris'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sifaris',
            name='mehsullar',
        ),
        migrations.RemoveField(
            model_name='sifaris',
            name='user',
        ),
        migrations.AddField(
            model_name='sifaris',
            name='cemi_mebleg',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sifaris',
            name='status',
            field=models.CharField(default='Yeni', max_length=50),
        ),
        migrations.CreateModel(
            name='SifarisMehsul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdar', models.PositiveIntegerField()),
                ('qiymet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mehsul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mehsullar.mehsul')),
                ('sifaris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mehsullar', to='mehsullar.sifaris')),
            ],
        ),
    ]