# Generated by Django 2.1.4 on 2019-01-06 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 6, 11, 34, 10, 392032)),
        ),
    ]