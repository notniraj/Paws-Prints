# Generated by Django 5.0.2 on 2024-02-22 22:10

import django.core.files.storage
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=50)),
                ('pet_type', models.CharField(max_length=50)),
                ('pet_breed', models.CharField(max_length=50)),
                ('pet_profile', models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='/media/photos'))),
                ('pet_color', models.CharField(blank=True, max_length=40, null=True)),
                ('pet_description', models.TextField(blank=True, null=True)),
                ('owner_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
