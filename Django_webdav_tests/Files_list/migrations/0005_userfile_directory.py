# Generated by Django 3.0 on 2020-03-08 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Files_list', '0004_auto_20200308_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='directory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Files_list.UserDirectory'),
        ),
    ]
