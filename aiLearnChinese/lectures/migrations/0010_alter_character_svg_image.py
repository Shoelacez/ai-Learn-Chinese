# Generated by Django 4.1.7 on 2023-03-24 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0009_rename_char_image_character_svg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='svg_image',
            field=models.TextField(null=True),
        ),
    ]
