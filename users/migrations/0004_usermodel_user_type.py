# Generated by Django 5.0.2 on 2024-02-16 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_status_usertype_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.usertype'),
        ),
    ]
