# Generated by Django 2.2.1 on 2019-05-14 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='dog_image',
            field=models.ImageField(default='dog_default.jpg', upload_to='dogs/'),
        ),
    ]
