# Generated by Django 3.0 on 2020-03-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0005_userfile_directory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='name',
            field=models.CharField(default='Untitled file', max_length=255),
        ),
    ]