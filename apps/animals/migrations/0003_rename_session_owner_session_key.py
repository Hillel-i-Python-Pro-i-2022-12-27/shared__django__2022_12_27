# Generated by Django 4.1.7 on 2023-03-14 18:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0002_owner_animal_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="owner",
            old_name="session",
            new_name="session_key",
        ),
    ]
