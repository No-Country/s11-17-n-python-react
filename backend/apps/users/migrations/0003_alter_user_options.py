# Generated by Django 4.2.6 on 2023-10-10 02:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_rename_user_name_user_username"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Usuario", "verbose_name_plural": "Usuarios"},
        ),
    ]