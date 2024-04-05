# Generated by Django 5.0.2 on 2024-03-02 22:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_petmodel_pet_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='petmodel',
            constraint=models.UniqueConstraint(fields=('owner', 'pet_name'), name='unique_owner_pet'),
        ),
    ]