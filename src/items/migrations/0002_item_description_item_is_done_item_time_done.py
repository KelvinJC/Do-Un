# Generated by Django 4.1.2 on 2022-10-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="item", name="is_done", field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="time_done",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
