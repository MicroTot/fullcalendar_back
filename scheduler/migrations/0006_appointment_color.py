# Generated by Django 3.2.8 on 2021-10-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20211014_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='color',
            field=models.CharField(default=3, max_length=20),
            preserve_default=False,
        ),
    ]
