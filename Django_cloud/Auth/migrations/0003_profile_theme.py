# Generated by Django 3.0 on 2020-04-09 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_auto_20200404_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='theme',
            field=models.IntegerField(choices=[(1, 'Thème clair'), (2, 'Thème sombre')], default=1),
        ),
    ]