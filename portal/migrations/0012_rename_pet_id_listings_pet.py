# Generated by Django 5.0.2 on 2024-04-21 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_listings_more_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='pet_id',
            new_name='pet',
        ),
    ]
