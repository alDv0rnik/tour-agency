# Generated by Django 5.0.4 on 2024-04-23 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_tourphotos_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourphotos',
            old_name='movie',
            new_name='tour',
        ),
    ]
