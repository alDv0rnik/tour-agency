# Generated by Django 5.0.4 on 2024-04-24 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderinfo_shipping_address_orderinfo_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='postal_code',
        ),
    ]