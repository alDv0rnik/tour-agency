# Generated by Django 5.0.4 on 2024-04-23 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_tourphotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourphotos',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tour_photos', to='catalog.tour'),
        ),
    ]
