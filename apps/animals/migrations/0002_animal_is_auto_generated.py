# Generated by Django 4.1.5 on 2023-02-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="is_auto_generated",
            field=models.BooleanField(default=False),
        ),
    ]
