# Generated by Django 4.1.7 on 2023-03-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lectures", "0004_listening"),
    ]

    operations = [
        migrations.AddField(
            model_name="listening",
            name="image",
            field=models.ImageField(
                default="default.jpg", upload_to="listening/images"
            ),
        ),
    ]
