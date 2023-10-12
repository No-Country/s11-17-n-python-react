# Generated by Django 4.2.6 on 2023-10-12 00:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("apps_profiles", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="created",
            field=models.DateTimeField(auto_now_add=True, default="2023-10-11"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
