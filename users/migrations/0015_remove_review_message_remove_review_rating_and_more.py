# Generated by Django 5.0.2 on 2024-04-19 08:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_review_delete_reviewsmodel'),
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='message',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.STAR_RATINGS_RATING_MODEL)),
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='users.review')),
            ],
        ),
    ]
