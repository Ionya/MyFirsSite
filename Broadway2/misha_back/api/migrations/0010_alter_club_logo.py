# Generated by Django 3.2 on 2023-04-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20230425_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='logo',
            field=models.CharField(default='https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg', max_length=1500),
        ),
    ]
