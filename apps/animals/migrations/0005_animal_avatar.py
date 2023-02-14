# Generated by Django 4.1.7 on 2023-02-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0004_alter_animal_kind"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="avatar",
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to="animals/animal/avatar/"),
        ),
    ]
