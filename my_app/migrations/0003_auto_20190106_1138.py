# Generated by Django 2.1.4 on 2019-01-06 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20190106_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 6, 11, 38, 22, 830097)),
        ),
    ]
