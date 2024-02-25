# Generated by Django 5.0.2 on 2024-02-21 20:08

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_usermodel_options_alter_usermodel_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='pet_picture',
            field=models.ImageField(default='img1', upload_to=django.core.files.storage.FileSystemStorage(location='/media/photos')),
        ),
    ]
