# Generated by Django 3.0 on 2020-03-11 13:33

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files_list', '0007_userdirectory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='directory',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.FileField(max_length=5000, storage=django.core.files.storage.FileSystemStorage(), upload_to=''),
        ),
        migrations.DeleteModel(
            name='UserDirectory',
        ),
    ]
