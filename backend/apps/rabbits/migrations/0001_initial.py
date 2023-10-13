# Generated by Django 4.2.6 on 2023-10-13 20:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apps_cages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rabbit",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("breed", models.CharField(max_length=20)),
                (
                    "genre",
                    models.CharField(
                        choices=[("Macho", "Macho"), ("Hembra", "Hembra")], max_length=6
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("tag", models.CharField(max_length=15, unique=True)),
                (
                    "weight",
                    models.DecimalField(decimal_places=1, default=1, max_digits=2),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("photo", models.CharField(blank=True, max_length=255)),
                (
                    "cage_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_cages.cage",
                    ),
                ),
            ],
        ),
    ]
