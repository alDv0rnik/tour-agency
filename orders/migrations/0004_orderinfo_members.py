# Generated by Django 5.0.4 on 2024-04-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_orderinfo_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='members',
            field=models.PositiveIntegerField(default=1, verbose_name='Members'),
        ),
    ]
