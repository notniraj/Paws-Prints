# Generated by Django 5.0.2 on 2024-04-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_review_rating_delete_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(default='Seen here.'),
            preserve_default=False,
        ),
    ]
