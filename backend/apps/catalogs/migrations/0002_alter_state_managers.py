# Generated by Django 4.2.6 on 2023-10-19 23:50

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("apps_catalogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="state",
            managers=[
                ("object_state", django.db.models.manager.Manager()),
            ],
        ),
    ]
