# Generated by Django 5.0.2 on 2024-04-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_listingcomments_listing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingcomments',
            name='downvotes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listingcomments',
            name='upvotes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]