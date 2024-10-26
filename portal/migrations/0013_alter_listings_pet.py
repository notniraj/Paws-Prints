# Generated by Django 5.0.2 on 2024-04-23 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_petmodel_unique_owner_pet'),
        ('portal', '0012_rename_pet_id_listings_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.petmodel'),
        ),
    ]
