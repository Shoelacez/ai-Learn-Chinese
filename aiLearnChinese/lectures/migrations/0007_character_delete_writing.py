# Generated by Django 4.1.7 on 2023-03-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0006_writing_remove_listening_lesson_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Writing',
        ),
    ]
