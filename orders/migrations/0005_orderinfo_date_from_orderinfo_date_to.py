# Generated by Django 5.0.4 on 2024-04-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderinfo_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='date_from',
            field=models.DateField(blank=True, null=True, verbose_name='Start date'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='date_to',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
    ]
