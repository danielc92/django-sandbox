# Generated by Django 2.2.1 on 2019-05-14 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190514_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_ct_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
