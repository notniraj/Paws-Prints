# Generated by Django 5.0.2 on 2024-04-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_petcaretip_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='more_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]