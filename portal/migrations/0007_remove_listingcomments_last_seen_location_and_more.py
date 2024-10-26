# Generated by Django 5.0.2 on 2024-04-05 09:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_remove_listings_is_found'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingcomments',
            name='last_seen_location',
        ),
        migrations.AddField(
            model_name='listingcomments',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='listingcomments',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listingcomments',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
