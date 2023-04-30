# Generated by Django 4.2 on 2023-04-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=500)),
                ("date_time", models.DateTimeField()),
                ("organizer", models.CharField(max_length=50)),
                ("likes", models.IntegerField(default=0)),
                ("dislikes", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Event",
                "verbose_name_plural": "Events",
            },
        ),
    ]