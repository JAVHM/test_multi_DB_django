# Generated by Django 4.2.4 on 2023-08-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Crash_Game",
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
                ("title", models.CharField(max_length=50, verbose_name="title")),
                ("content", models.CharField(max_length=50, verbose_name="content")),
                ("app_name", models.CharField(max_length=50, verbose_name="app_name")),
            ],
        ),
    ]
