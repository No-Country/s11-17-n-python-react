# Generated by Django 4.2.6 on 2023-10-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps_cages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cage",
            name="total_weight",
            field=models.IntegerField(default=0),
        ),
    ]