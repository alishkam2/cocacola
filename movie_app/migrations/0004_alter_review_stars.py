# Generated by Django 5.1.3 on 2024-12-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0003_review_stars"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.PositiveIntegerField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
            ),
        ),
    ]
