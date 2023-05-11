# Generated by Django 4.2.1 on 2023-05-11 18:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Queue",
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
                ("section_code", models.CharField(max_length=5)),
                ("section_name", models.TextField()),
                ("division_code", models.CharField(max_length=5)),
                ("division_name", models.TextField()),
                ("group_code", models.CharField(max_length=10)),
                ("group_name", models.TextField()),
                ("class_code", models.CharField(max_length=10)),
                ("class_name", models.TextField()),
                ("subclass_code", models.CharField(max_length=15)),
                ("subclass_name", models.TextField()),
            ],
        ),
    ]