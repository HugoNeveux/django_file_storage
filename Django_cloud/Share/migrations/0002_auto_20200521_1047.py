# Generated by Django 3.0 on 2020-05-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Share', '0001_squashed_0002_auto_20200520_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharelink',
            name='file_path',
            field=models.CharField(max_length=2000),
        ),
    ]
