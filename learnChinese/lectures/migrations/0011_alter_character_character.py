# Generated by Django 4.1.7 on 2023-03-24 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0010_alter_character_svg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character',
            field=models.CharField(max_length=10),
        ),
    ]
