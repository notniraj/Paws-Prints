# Generated by Django 5.0.2 on 2024-02-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_rename_status_listings_is_found_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='date_found',
            field=models.DateField(blank=True, null=True),
        ),
    ]
