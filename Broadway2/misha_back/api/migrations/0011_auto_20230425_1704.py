# Generated by Django 3.2 on 2023-04-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_club_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.CharField(default='https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg', max_length=1500),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.CharField(default='https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg', max_length=1500),
        ),
    ]
