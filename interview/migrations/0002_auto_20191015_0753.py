# Generated by Django 2.1.7 on 2019-10-15 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.DateField(default=datetime.date(2019, 10, 15)),
        ),
    ]
