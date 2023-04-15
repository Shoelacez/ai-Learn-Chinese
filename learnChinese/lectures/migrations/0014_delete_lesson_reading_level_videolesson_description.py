# Generated by Django 4.1.7 on 2023-03-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0013_videolesson_delete_character'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.AddField(
            model_name='reading',
            name='level',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='videolesson',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
