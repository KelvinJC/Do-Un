# Generated by Django 4.1.2 on 2022-10-06 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("activity", models.CharField(max_length=100)),
                (
                    "time_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
