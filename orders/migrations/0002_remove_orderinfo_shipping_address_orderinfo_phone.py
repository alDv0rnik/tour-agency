# Generated by Django 5.0.4 on 2024-04-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=200, verbose_name='Phone'),
        ),
    ]